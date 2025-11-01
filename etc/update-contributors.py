#!/usr/bin/env python3

# Standard library
import json
import os
from email.utils import parseaddr
import subprocess
import sys
import unicodedata

# Third-party
import requests
import yaml



##########################################
# 1. Constants
##########################################

API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()

PEOPLE_LIST_FILE = "../_data/people_list.yml"
SUMMARY_FILE = "../summary.txt"
REPOS_DIR = "repos"

BOT_TOKENS = ("github-actions[bot]", "dependabot[bot]", "renovate[bot]", "changelog[bot]")

GIT_LOG_SINCE = "--since=1 year ago"
GIT_LOG_FORMAT_1 = "--format=%aN <%aE>%n%(trailers:unfold,key=Co-authored-by)"
GIT_LOG_FORMAT_2 = "--format=%H %s %(trailers:key=Co-authored-by)"

REPO_LIST = [
    "Nemocas/AbstractAlgebra.jl",
    "algebraic-solving/AlgebraicSolving.jl",
    "oscar-system/GAP.jl",
    "thofma/Hecke.jl",
    "Nemocas/Nemo.jl",
    "oscar-system/Oscar.jl",
    "oscar-system/Polymake.jl",
    "oscar-system/Singular.jl",
]

STATUS_PI = "pi" # not used yet
STATUS_ACTIVE = "active" # not used yet
STATUS_RETIRED = "retired" # not used yet

SORT_WEIGHT = {
    "name": 0,
    "affiliation": 1,
    "email": 2,
    "github": 3,
    "website": 4,
    "paid_by_dfg": 5,
    "status": 6,
    "comment": 7,
    "aka": 8,
    "aka_email": 9,
    "repos": 10,
}

def custom_sort_function(item):
    name, _ = item
    sortweight = SORT_WEIGHT
    return sortweight[name]



##########################################
# 2. Read information from people_list.yml
##########################################

try:
    with open(PEOPLE_LIST_FILE, "r", encoding="utf-8") as ymlfile:
        current_contributors = yaml.safe_load(ymlfile) or []
except FileNotFoundError:
    print(f"Error: Could not find {PEOPLE_LIST_FILE}")
    sys.exit(1)
except yaml.YAMLError as e:
    print(f"Error parsing YAML file {PEOPLE_LIST_FILE}: {e}")
    sys.exit(1)

for person in current_contributors:
    person.setdefault("repos", [])

current_github_usernames = [person["github"] for person in current_contributors if "github" in person]



##########################################
# 3. Build fast alias lookup
##########################################

email_owner = {}  # lowercased email -> person dict
name_owner  = {}  # normalized name -> person dict

def _norm_name(s: str) -> str:
    return " ".join((s or "").split()).lower()

for p in current_contributors:
    # index primary + aka emails
    emails = []
    if p.get("email"):
        emails.append(p["email"])
    if p.get("aka_email"):
        emails.extend(p["aka_email"] or [])
    for e in emails:
        email_owner[e.lower()] = p

    # index primary + aka names
    names = []
    if p.get("name"):
        names.append(p["name"])
    if p.get("aka"):
        names.extend(p["aka"] or [])
    for n in names:
        name_owner[_norm_name(n)] = p

# Helper function to be used below
def _person_key(name: str, email: str):
    owner = email_owner.get(email.lower()) or name_owner.get(_norm_name(name))
    if owner and owner.get("github"):
        return ("gh", owner["github"])
    if owner and (owner.get("email") or email):
        # canonicalize to the owner's primary email if present
        base = (owner.get("email") or email).lower()
        return ("email", base)
    return ("email", email.lower())



##########################################
# 4. Collect (co)authors for each repo
##########################################

# 4.1 Change into REPOS_DIR
if not os.path.isdir(REPOS_DIR):
    os.mkdir(REPOS_DIR)
os.chdir(REPOS_DIR)

# 4.2 Run over repos to aggreate authors and coauthors
summarystring = ""
aggregate = {}      # key -> {'name','email','is_author','known_github','repos': set()}
for repo in REPO_LIST:

    print(f"Processing {repo}...")
    repo_path = repo.split('/')[-1]
    if not os.path.isdir(repo_path):
        subprocess.run(["git", "clone", f"https://github.com/{repo}"], check=True)
    os.chdir(repo_path)
    subprocess.run(["git", "fetch", "--all"], check=True)
    subprocess.run(["git", "pull"], check=True)
    log_cmd = ["git", "log", "--use-mailmap", GIT_LOG_SINCE, GIT_LOG_FORMAT_1]
    res = subprocess.run(log_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    os.chdir("..")
    if res.returncode != 0:
        print("DEBUG git log failed; stderr:", res.stderr.strip())
        sys.exit(1)
    
    # 4.5 Process the log and update aggregate accordingly
    for raw in res.stdout.splitlines():

        # Prepare the line and skip if empty
        line = raw.strip()
        if not line:
            continue

        # Identify co-authors
        is_author = True
        if line.lower().startswith("co-authored-by:"):
            line = line.split(":", 1)[1].strip()
            is_author = False

        # Skip bots and non-address lines
        lower_line = line.lower()
        if any(b in lower_line for b in BOT_TOKENS):
            continue
        if "[bot]" in lower_line:
            summarystring += f"- Skipping suspected bot line in {repo}: {line!r}\n"
            continue
        if "<" not in line or ">" not in line:
            summarystring += f"- Skipping non-address line in {repo}: {line!r}\n"
            continue

        # Parse "Name <email>"
        name, email = parseaddr(line)
        name = " ".join(unicodedata.normalize("NFKC", name).split())
        email = unicodedata.normalize("NFKC", email).strip()

        # Validate
        if not email and not name:
            summarystring += f"- Missing name and email in {repo}; line={line!r}; skipping\n"
            continue
        if not email:
            summarystring += f"- Missing email for '{name}' in {repo}; skipping\n"
            continue
        if not name:
            summarystring += f"- Missing name for '{email}' in {repo}; skipping\n"
            continue

        # Alias resolution from PEOPLE_LIST_FILE (aka/aka_email)
        owner = email_owner.get(email.lower()) or name_owner.get(_norm_name(name))
        known_github = owner.get("github") if owner else None

        # Person key: prefer github if known; else canonical email via owner; else raw email
        key = _person_key(name, email)

        # Update aggregate (one record per person across all repos)
        rec = aggregate.get(key)
        if rec is None:
            aggregate[key] = {
                "name": name,
                "email": email,
                "is_author": bool(is_author),
                "known_github": known_github,
                "repos": set([repo]),
            }
        else:
            # promote to author if any occurrence is an author
            if not rec["is_author"] and is_author:
                rec["is_author"] = True
            # accumulate repos
            rec["repos"].add(repo)
            # fill github if we learn it now
            if known_github and not rec["known_github"]:
                rec["known_github"] = known_github
            # prefer non-noreply email (often comming with nicely formatted name, which we therefore update)
            if "users.noreply.github.com" in rec["email"] and "users.noreply.github.com" not in email:
                rec["name"], rec["email"] = name, email



##########################################
# 5. Processing further
##########################################

unresolved = []
newList = []
newpersonlist = []
github_newusers = []
github_userlist = []
for key, rec in aggregate.items():
    name = rec["name"]
    email = rec["email"]
    repos = sorted(rec["repos"])
    gh = rec["known_github"]

    if gh:
        # Known GitHub from YAML
        if gh in current_github_usernames:
            # existing contributor: just append repos
            user = next((it for it in current_contributors if it.get("github") == gh), None)
            if user is not None:
                for r in repos:
                    if r not in user.setdefault("repos", []):
                        user["repos"].append(r)
        else:
            # new contributor (known gh from aliases)
            newpersonlist.append(name)
            github_newusers.append(gh)
            newList.append([name, email, gh, repos])
        if gh not in github_userlist:
            github_userlist.append(gh)
    else:
        # No GitHub yet — leave for a later step (or future API pass)
        unresolved.append(rec)

# Optional: note unresolved folks so they don't silently vanish
for rec in unresolved:
    summarystring += (
        f"- Github username not found for {rec['name']} <{rec['email']}>; "
        f"repos={sorted(rec['repos'])}. Skipping for now.\n"
    )



##########################################
# 6. Sort as new, retired, active
##########################################

newCoauthorList = []

# mark active / retired
# if PI, don't touch them
os.chdir("..")
retcount = 0
revcount = 0
retpersonlist = []
revpersonlist = []
for i in current_contributors:
    if 'github' not in i:
        #co authors
        continue
    if i['status']=='pi':
        continue
        #don't touch a thing!
    elif i['github'] in github_userlist:
        if i['status'] == 'retired':
            revcount += 1
            revpersonlist.append(i['name'])
        i['status'] = 'active'
    else:
        if i['status'] == 'active':
            retcount += 1
            retpersonlist.append(i['name'])
        i['status'] = 'retired'

np = []
for i in newList:
    if "users.noreply.github.com" in i[1]:
        np.append({"name": i[0], "github": i[2], "status": "active", "repos": i[3]})
        summarystring += f"- Email not found for {i[0]} ({i[2]})..!\n"
    else:
        np.append({"name": i[0], "email": i[1], "github": i[2], "status": "active", "repos": i[3]})
current_contributors.extend(np)

np = []
for i in newCoauthorList:
    np.append({"name": i[0], "email": i[1], "status": "active", "comment": f"Co-author of commit {i[3]}","repos": [i[2]]})
current_contributors.extend(np)

sortedcurrent_contributors = sorted(current_contributors, key= lambda d: d['name'].split()[-1])



##########################################
# 7. Save the findings
##########################################

# save yml to *NEW* file
# how inefficient is list comprehension ?
pilist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedcurrent_contributors if i['status'] == "pi"]
activelist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedcurrent_contributors if i['status'] == "active"]
retiredlist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedcurrent_contributors if i['status'] == "retired"]

# Hack copied from https://github.com/yaml/pyyaml/issues/127#issuecomment-525800484
class MyDumper(yaml.SafeDumper):
    # HACK: insert blank lines between top-level objects
    # inspired by https://stackoverflow.com/a/44284819/3786245
    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1:
            super().write_line_break()

# Write people_list.yml
with open('../_data/people_list.yml', 'w') as outfile:
    outfile.write("# It is possible that people marked as 'retired' may have the repo key as an "
                  "empty array.\n# This is because people are marked as retired if the update "
                  "script could not find them in any repo.\n# Retired people only have repo "
                  "information if repo information about them was known when they were\n# active "
                  "(or manually added) by a maintainer.\n\n")
    yaml.dump(sortedcurrent_contributors, outfile, Dumper=MyDumper, sort_keys = False, allow_unicode=True)

# Produce summary
summarystring = f"""This PR updates the contributors list based on the latest changes.
New contributors : {len(newpersonlist)} | {newpersonlist}
Revived contributors : {revcount} | {revpersonlist}
Newly retired contributors : {retcount} | {retpersonlist}
New co-authors : {len(newCoauthorList)} | {newCoauthorList}
\nSummary Notes:\n\n"""+ summarystring
with open(SUMMARY_FILE, 'w') as summaryfile:
    summaryfile.write(summarystring)
