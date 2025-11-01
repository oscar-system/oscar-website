#!/usr/bin/env python3

# Standard library
import json
import os
from email.utils import parseaddr
import re
import subprocess
import sys
import unicodedata

# Third-party
import requests
import yaml



##########################################
# 1. Constants (static configuration)
##########################################

# Derive absolute paths once so chdir() doesn’t bite us later.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
REPOS_DIR = os.path.join(PROJECT_ROOT, "repos")
PEOPLE_LIST_FILE = os.path.join(PROJECT_ROOT, "_data", "people_list.yml")
SUMMARY_FILE = os.path.join(PROJECT_ROOT, "summary.txt")

# Auth
API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()

# Git config
GIT_LOG_SINCE = "--since=1 year ago"
GIT_LOG_FORMAT_1 = "--format=%aN <%aE>%n%(trailers:unfold,key=Co-authored-by)"
GIT_LOG_FORMAT_2 = "--format=%H %(trailers:only,unfold,separator=|,key=Co-authored-by) %s"

# Repositories to scan (tuple to emphasize immutability)
REPO_LIST = (
    "Nemocas/AbstractAlgebra.jl",
    "algebraic-solving/AlgebraicSolving.jl",
    "oscar-system/GAP.jl",
    "thofma/Hecke.jl",
    "Nemocas/Nemo.jl",
    "oscar-system/Oscar.jl",
    "oscar-system/Polymake.jl",
    "oscar-system/Singular.jl",
)

# Bots we ignore
BOT_TOKENS = (
    "github-actions[bot]",
    "dependabot[bot]",
    "renovate[bot]",
    "changelog[bot]",
)

# Regexes
HASH_RE = re.compile(r"\b[0-9a-f]{40}\b", re.I)

# Display/sort preferences
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



##########################################
# 2. Globals (runtime state; mutated)
##########################################

# Contributor lists
current_contributors = []  # list[dict]

# Alias indices built from current_contributors
email_owner = {}   # lowercased email -> person dict
name_owner  = {}   # normalized name  -> person dict

# Aggregate across repos: key -> {'name','email','is_author','known_github','repos': set()}
aggregate = {}

# Collected notes (maybe use a list to avoid 'global' rebinding of strings)
summarystring = ""

# Once we aggregated the current contributors, we fill them into the following buckets
active_contributors = []            # references to active current_contributors entries
new_contributors = []               # data of new (co)authors in unified schema: {"name","email","repos","github|None","commit_hash|None"}
_seen_current = set()               # track object identity for computation of retired contributors
retired_contributors = []           # references to retired current_contributors entries
sorted_current_contributors = []    # the current contributors - new active, retired, PI sorted by name
ordered_people = []                 # final list of sorted current contributors, with each field sorted by our custom design in SORT_WEIGHT



##########################################
# 3. Read information from people_list.yml
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



##########################################
# 4. Build fast alias lookup
##########################################

def _norm_name(s: str) -> str:
    return " ".join((s or "").split()).lower()

for p in current_contributors:
    # index primary + aka emails
    emails = []
    if p.get("email"):
        emails.append(p["email"])
    if p.get("aka_email"):
        emails.extend(p["aka_email"])
    for e in emails:
        email_owner[e.lower()] = p

    # index primary + aka names
    names = []
    if p.get("name"):
        names.append(p["name"])
    if p.get("aka"):
        names.extend(p["aka"])
    if p.get("github"):
        names.append(p["github"])
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
# 5. Helper: Process git log
##########################################

def process_log_into_aggregate(res: str, repo: str) -> None:

    global summarystring, aggregate, email_owner, name_owner

    for raw in res.splitlines():

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
# 6. Find (co)authors of all repos
##########################################

if not os.path.isdir(REPOS_DIR):
    os.mkdir(REPOS_DIR)
os.chdir(REPOS_DIR)
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
    process_log_into_aggregate(res.stdout, repo)



##########################################
# 7. Helpers to find (co)-author details
##########################################

# Try to resolve a GitHub login by finding one authored commit for this email.
def resolve_github_via_commit(email: str, repos: list[str]) -> str | None:
    if not email:
        return None
    for r in repos:
        repo_path = r.split('/')[-1]
        # Find a representative commit authored by this email
        res = subprocess.run(["git", "log", GIT_LOG_SINCE, f"--author={email}", "--format=%H", "-n", "1"],
                           cwd=repo_path, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            continue
        commit_hash = (res.stdout or "").strip()
        if not commit_hash:
            continue  # no direct authored commit in this repo (could be co-author only)
        url = f"https://api.github.com/repos/{r}/commits/{commit_hash}"
        resp = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
        if resp.status_code != 200:
            continue
        author = resp.json().get("author")
        if author and author.get("login"):
            return author["login"]
    return None

# Try to resolve a GitHub login by finding one co-authored commit for this email.
def find_coauthor_commit(name: str, email: str, repos: list[str]) -> tuple[str | None, str | None]:
    targets = {t for t in (name.lower(), email.lower()) if t}
    for r in repos:
        repo_path = r.split('/')[-1]
        res = subprocess.run(["git", "log", GIT_LOG_SINCE, GIT_LOG_FORMAT_2],
                             cwd=repo_path, capture_output=True, text=True, encoding="utf-8")
        if res.returncode != 0:
            continue
        for line in res.stdout.splitlines():
            low = line.lower()
            if not any(t in low for t in targets):
                continue
            m = HASH_RE.search(line)
            if m:
                return m.group(0)
    return "(no hash found)"



##########################################
# 8. Post-aggregation enrichment & updates
##########################################

for key, rec in aggregate.items():
    name  = rec["name"]
    email = rec["email"]
    repos = rec["repos"]
    gh    = rec.get("known_github") or resolve_github_via_commit(email, repos)
    user = (name_owner.get(gh) or (email and email_owner.get(email.lower())) or name_owner.get(_norm_name(name)))

    # Existing contributor
    if user:
        # Merge repos into existing user (preserve order, avoid dups)
        have = set(user["repos"])
        user["repos"].extend(r for r in repos if r not in have)

        # If we just learned their GitHub, store it and index it
        if gh and not user.get("github"):
            user["github"] = gh
            name_owner[gh] = user

        # Mark active once
        uid = id(user)
        if uid not in _seen_current:
            _seen_current.add(uid)
            active_contributors.append(user)

    # Brand-new person; authors & coauthors treated uniformly
    else:
        if gh:  # New "author"
            new_contributors.append({"name": name, "email": email, "repos": repos, "github": gh, "commit_hash": None})
        else:   # New "coauthor" — resolve a representative commit immediately
            commit_hash = find_coauthor_commit(name, email, repos)
            new_contributors.append({"name": name, "email": email, "repos": repos, "github": None, "commit_hash": commit_hash})

# Retired = in current_contributors but not seen in this run
retired_contributors = [p for p in current_contributors if id(p) not in _seen_current]



##########################################
# 9. Update YAML structure
##########################################

_prev_status = {id(p): p.get("status") for p in current_contributors}

for rec in new_contributors:
    newp = {"name": rec["name"], "email": rec["email"], "repos": sorted(set(rec["repos"])), "status": "active"}
    if rec["github"]:
        newp["github"] = rec["github"]
    else:
        newp["comment"] = f"Co-author of commit {rec['commit_hash']}"
    current_contributors.append(newp)

for p in active_contributors:
    p["status"] = "active"

for p in retired_contributors:
    if p.get("status") != "pi":
        p["status"] = "retired"

for p in current_contributors:
    p["repos"] = sorted(set(p["repos"]))

sorted_current_contributors = sorted(current_contributors, key=lambda d: (d.get("name", "").split()[-1], d.get("name", "")))

def custom_sort_function(item):
    key, _ = item
    return SORT_WEIGHT.get(key, 999)

ordered_people = [dict(sorted(person.items(), key=custom_sort_function)) for person in sorted_current_contributors]



##########################################
# 10. Save the findings to YML file
##########################################

class MyDumper(yaml.SafeDumper):
    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()

with open(PEOPLE_LIST_FILE, "w", encoding="utf-8") as outfile:
    outfile.write(
        "# It is possible that people marked as 'retired' may have the repo key as an empty array.\n"
        "# This is because people are marked as retired if the update script could not find them in any repo.\n"
        "# Retired people only have repo information if repo information about them was known when they were\n"
        "# active (or manually added) by a maintainer.\n\n"
    )
    yaml.dump(ordered_people, outfile, Dumper=MyDumper, sort_keys=False, allow_unicode=True)



##########################################
# 11. Write summary text
##########################################

new_names = [rec["name"] for rec in new_contributors]
newly_retired_names = [p.get("name") for p in retired_contributors if _prev_status.get(id(p)) == "active"]

summarystring = (
    "This PR updates the contributors list based on the latest changes.\n"
    f"New contributors : {len(new_names)} | {new_names}\n"
    f"Newly retired contributors : {len(newly_retired_names)} | {newly_retired_names}\n\n"
    "Summary Notes:\n\n"
) + summarystring

with open(SUMMARY_FILE, "w", encoding="utf-8") as summaryfile:
    summaryfile.write(summarystring)
