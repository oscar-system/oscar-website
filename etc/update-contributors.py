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
# 3. Collect (co)authors for each repo
##########################################

# 3.1 Change into REPOS_DIR
if not os.path.isdir(REPOS_DIR):
    os.mkdir(REPOS_DIR)
os.chdir(REPOS_DIR)

# 3.2 Initialize variables
newList = []
newCoauthorList = []
namelist = []
newpersonlist = []
github_newusers = []
github_userlist = []
github_username = '__notfound__'
summarystring = ""

# 3.3 Run over repos
for repo in REPO_LIST:

    print("\n")
    print("-------------------------------")
    print(f"Processing {repo}...")
    print("-------------------------------")
    print("\n")

    # 3.4 Clone the repository/fetch the latest updates
    print("Fetching updates...\n")
    repo_path = repo.split('/')[-1]
    if not os.path.isdir(repo_path):
        subprocess.run(["git", "clone", f"https://github.com/{repo}"], check=True)
    os.chdir(repo_path)
    subprocess.run(["git", "fetch", "--all"], check=True)
    subprocess.run(["git", "pull"], check=True)

    # 3.5 Obtain the log from github
    print("Generating list of authors active in past year...\n\n")
    log_cmd = ["git", "log", "--use-mailmap", GIT_LOG_SINCE, GIT_LOG_FORMAT_1]
    res = subprocess.run(log_cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode != 0:
        print("DEBUG git log failed; stderr:", res.stderr.strip())
        sys.exit(1)
    
    # 3.6 Process the log, so we obtain pairs of author names and their emails
    # Expected lines include:
    #   Cool Author <cool-author-email>
    #   Co-authored-by: Also Cool <another email>
    by_email = {}        # email_lower -> (name, email, is_author)
    for raw in res.stdout.splitlines():

        # Initial processing of the line and skipping if needed
        line = raw.strip()
        is_author = True
        if line.lower().startswith("co-authored-by:"):
            line = line.split(":", 1)[1].strip()
            is_author = False
        if not line:
            continue
        lower_line = line.lower()
        if any(b in lower_line for b in ("github-actions[bot]", "dependabot[bot]", "renovate[bot]", "changelog[bot]")):
            continue
        if "[bot]" in lower_line:
            summarystring += f"- Skipping expected bot line in {repo}: {line!r}\n"
            continue
        if "<" not in line or ">" not in line:
            summarystring += f"- Skipping non-address line in {repo}: {line!r}\n"
            continue
        
        # Parse to obtain name and email
        name, email = parseaddr(line)
        name = " ".join(unicodedata.normalize("NFKC", name).split())
        email = unicodedata.normalize("NFKC", email).strip()
        
        # Validate
        if (not email) and (not name):
            summarystring += f"- Missing name and email in {repo}; line={line!r}; skipping\n"
            continue
        if not email:
            summarystring += f"- Missing email for '{name}' in {repo}; skipping\n"
            continue
        if not name:
            summarystring += f"- Missing name for '{email}' in {repo}; skipping\n"
            continue

        # Dedupe
        key = email.lower()
        prev = by_email.get(key)
        if prev is None:
            by_email[key] = (name, email, is_author)
        else:
            # upgrade to author if any occurrence is an author
            if is_author and not prev[2]:
                by_email[key] = (name, email, True)
    
    # Stable, human-friendly order: by name (case-insensitive), then email
    triples = set(by_email.values())
    dnamelist = [[n, e, is_a] for (n, e, is_a) in sorted(triples, key=lambda t: (t[0].lower(), t[1], not t[2]))]
    namelist.extend(dnamelist)
    
    # 3.7 Process dnamelist further - somehow...
    count = 0
    for i in dnamelist:
        count = count+1
        print(f"Item {count} of {len(dnamelist)}...")
        print(i)
        email = i[1]
        process = subprocess.run(['git', 'log', f'--author={email}', '--format=%H', '-n 1'],
                                   capture_output=True)
        hash = process.stdout.decode().strip()
        github_commit_url = f"https://api.github.com/repos/{repo}/commits/{hash}"
        #ask github API for username
        r = requests.get(github_commit_url, headers={"Authorization":f"Bearer {API_KEY}"})
        if r.status_code == 200:
            j = json.loads(r.text)
            github_username = '__notfound__'
            if j['author'] == None:
                # this commit was authored by someone and committed by someone else
                # so github can't find a github user for the author, only for committed
                # so we go through our list entire people list and see if we know the combination of
                # name and email already
                # or if the name exists in an aka
                # or if the email exists in aka_email
                flag = False
                for person in current_contributors:
                    if 'email' in person.keys() and 'name' in person.keys():
                        if i[0] == person['name'] and i[1] == person['email']:
                            # we know the person, check if we know the github ID
                            if 'github' in person.keys() and person['github'] != '':
                                # we know the person and the github, just mark person as active
                                github_username = person['github']
                                flag = True
                                break
                        elif "aka" in person:
                            # the person has an alias
                            if i[0] in person["aka"]:
                                if 'github' in person.keys() and person['github'] != '':
                                    # we know the person and the github, just mark person as active
                                    github_username = person['github']
                                    flag = True
                                    break
                        elif "aka_email" in person:
                            # the person has an alias email
                            if i[1] in person["aka_email"]:
                                if 'github' in person.keys() and person['github'] != '':
                                    # we know the person and the github, just mark person as active
                                    github_username = person['github']
                                    flag = True
                                    break
                if not flag:
                    summarystring += f"- Github username not found for {i[0]} with email {i[1]}. Excluding from people_list.yml\n"
                    continue
            if github_username == '__notfound__':
                github_username = j['author']['login']
        elif github_commit_url == f"https://api.github.com/repos/{repo}/commits/":
            # this is a case of a co-author
            flag = False
            for person in current_contributors:
                if 'email' in person.keys() and 'name' in person.keys():
                    if i[0] == person['name'] and i[1] == person['email']:
                            flag = True
                            break
                    elif "aka" in person:
                        # the person has an alias
                        if i[0] in person["aka"]:
                            if 'github' in person.keys() and person['github'] != '':
                                # we know the person and the github, just mark person as active
                                github_username = person['github']
                                flag = True
                                break
                    elif "aka_email" in person:
                        # the person has an alias email
                        if i[1] in person["aka_email"]:
                            if 'github' in person.keys() and person['github'] != '':
                                # we know the person and the github, just mark person as active
                                github_username = person['github']
                                flag = True
                                break
                    elif i[0] == person['name'] or i[1] == person['email']:
                        github_username = person['github']
                        flag = True
                        break
            if not flag:
                # a co-author we don't know about at all - find a commit hash that mentions them
                res = subprocess.run(["git", "log", GIT_LOG_SINCE, GIT_LOG_FORMAT_2],capture_output=True, text=True)
                if res.returncode != 0:
                    print("ERROR: git log for co-author failed:", res.stderr.strip())
                    exit(1)
                commit_hash = None
                target_lower = {i[0].lower(), i[1].lower()}
                for line in res.stdout.splitlines():
                    lower = line.lower()
                    if any(t in lower for t in target_lower):
                        parts = line.split()
                        if parts:
                            commit_hash = parts[0]
                            break
                if commit_hash == None:
                    print(f"ERROR: Could not find a commit hash for co-author {i[0]} <{i[1]}> in {repo}")
                    exit(1)
                newCoauthorList.append([i[0], i[1], repo, commit_hash])
        else:
            # this will never happen, except if the API lies to you
            # or blocks access
            print(r.status_code)
            print(r)
            print(r.text)
            print(email)
            print(github_commit_url)
            github_username = "__notfound__"
            flag = False

        assert github_username != "__notfound__"
        if github_username not in current_github_usernames and github_username not in github_newusers and github_username != "__notfound__":
            print("A new contributor!")
            newpersonlist.append(i[0])
            print(f"{i[0]}\t{i[1]}\t{github_username}")
            github_newusers.append(github_username)
            newList.append([i[0], i[1], github_username, [repo]])
        elif github_username in current_github_usernames:
            user = [item for item in current_contributors if 'github' in item and item['github'] == github_username][0]
            if repo not in user['repos']:
                user['repos'].append(repo)
        else:
            # github_username in github_newusers
            user = [item for item in newList if item[2] == github_username][0]
            if repo not in user[3]:
                user[3].append(repo)
        if github_username not in github_userlist:
            github_userlist.append(github_username)
    os.chdir("..")



##########################################
# 4. Sort as new, retired, active
##########################################

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
# 5. Save the findings
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
