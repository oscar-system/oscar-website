#!/usr/bin/env python3

# Standard library
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

# Contributor lists and index structures
current_contributors = []  # loaded from YAML
email_owner = {}           # lowercased email → person dict
name_owner = {}            # normalized name → person dict

# Aggregation state
aggregate = {}
summarystring = ""

# Classification buckets
active_contributors, new_contributors, retired_contributors = [], [], []
_seen_current = set()



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
    return " ".join((s or "").split()).casefold()

for p in current_contributors:
    if p.get("email"):
        email_owner[p.get("email").casefold()] = p
    for ae in (p.get("aka_email") or ()):
        email_owner[ae.casefold()] = p
    if p.get("name"):
        name_owner[_norm_name(p.get("name"))] = p
    for an in (p.get("aka") or ()):
        name_owner[_norm_name(an)] = p
    if p.get("github"):
        name_owner[_norm_name(p.get("github"))] = p

def lookup_user(gh, email, name):
    return ((gh and name_owner.get(_norm_name(gh))) or (email and email_owner.get(email.casefold())) or name_owner.get(_norm_name(name)))



##########################################
# 5. Helper: Process git log
##########################################

def process_log_into_aggregate(res: str, repo: str) -> None:
    global summarystring, aggregate  #, email_owner, name_owner
    for raw in res.splitlines():
        line = raw.strip()
        if not line: continue

        if line.lower().startswith("co-authored-by:"):
            line = line.split(":", 1)[1].strip()

        low = line.lower()
        if any(b in low for b in BOT_TOKENS):
            continue
        if "[bot]" in low:
            summarystring += f"- Skipping suspected bot line in {repo}: {line!r}\n"
            continue
        if "<" not in line or ">" not in line:
            summarystring += f"- Skipping non-address line in {repo}: {line!r}\n"
            continue

        name, email = parseaddr(line)
        name  = " ".join(unicodedata.normalize("NFKC", name).split())
        email = unicodedata.normalize("NFKC", email).strip()
        if not email or not name:
            summarystring += f"- Missing {'email' if not email else 'name'} for {name or email} in {repo}; skipping\n"
            continue

        owner = email_owner.get(email.casefold()) or name_owner.get(_norm_name(name))
        known_github = owner.get("github") if owner else None
        key = ("gh", known_github.lower()) if known_github else ("email", ((owner and owner.get("email")) or email).casefold())

        rec = aggregate.get(key)
        if rec is None:
            aggregate[key] = {"name": name, "email": email, "known_github": known_github, "repos": {repo}}
        else:
            rec["repos"].add(repo)
            if known_github and not rec["known_github"]:
                rec["known_github"] = known_github
            if "users.noreply.github.com" in rec["email"] and "users.noreply.github.com" not in email:
                rec["name"], rec["email"] = name, email



##########################################
# 6. Find (co)authors of all repos
##########################################

def _repo_dir(repo_full: str) -> str:
    return os.path.join(REPOS_DIR, repo_full.split('/')[-1])

os.makedirs(REPOS_DIR, exist_ok=True)
for repo in REPO_LIST:
    print(f"Processing {repo}...")
    repo_dir = _repo_dir(repo)
    if not os.path.isdir(repo_dir):
        subprocess.run(["git", "clone", f"https://github.com/{repo}", repo_dir], check=True)
    else:
        subprocess.run(["git", "-C", repo_dir, "pull", "--ff-only"], check=True)
    res = subprocess.run(
        ["git", "-C", repo_dir, "log", "--use-mailmap", GIT_LOG_SINCE, GIT_LOG_FORMAT_1],
        check=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    process_log_into_aggregate(res.stdout, repo)



##########################################
# 7. Helpers to find (co)-author details
##########################################

# Try to resolve a GitHub login by finding one authored commit for this email.
def resolve_github_via_commit(email: str, repos: list[str]) -> str | None:
    if not email:
        return None
    for r in repos:
        res = subprocess.run(
            ["git", "-C", _repo_dir(r), "log", GIT_LOG_SINCE, f"--author={email}", "--format=%H", "-n", "1"],
            check=True, capture_output=True, text=True, encoding="utf-8")
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
def find_coauthor_commit(name: str, email: str, repos: list[str]) -> str:
    targets = {t for t in (name.lower(), email.lower()) if t}
    for r in repos:
        res = subprocess.run(
            ["git", "-C", _repo_dir(r), "log", GIT_LOG_SINCE, GIT_LOG_FORMAT_2],
            check=True, capture_output=True, text=True, encoding="utf-8")
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
    user = lookup_user(gh, email, name)

    # Existing contributor
    if user:
        # Merge repos into existing user (preserve order, avoid dups)
        have = set(user["repos"])
        user["repos"].extend([r for r in repos if r not in have])

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
# 9. Apply updates and dump output
##########################################

# Find the newly retired contributors
_prev_status = {id(p): p.get("status") for p in current_contributors}
newly_retired_names = [p.get("name") for p in retired_contributors if _prev_status.get(id(p)) == "active"]

# Apply updates
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

# Normalize repos list deterministically
for p in current_contributors:
    p["repos"] = sorted(set(p["repos"]))

# Final order by surname, then tidy field order
people_sorted = sorted(current_contributors, key=lambda d: (d.get("name", "").split()[-1], d.get("name", "")))
ordered_people = [dict(sorted(p.items(), key=lambda kv: SORT_WEIGHT.get(kv[0], 999))) for p in people_sorted]

# Write new content to PEOPLE_LIST_FILE
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

# Create summary in SUMMARY_FILE
new_names = [rec["name"] for rec in new_contributors]
summary = (
    "This PR updates the contributors list based on the latest changes.\n"
    f"New contributors : {len(new_names)} | {new_names}\n"
    f"Newly retired contributors : {len(newly_retired_names)} | {newly_retired_names}\n\n"
    "Summary Notes:\n\n"
) + summarystring
with open(SUMMARY_FILE, "w", encoding="utf-8") as summaryfile:
    summaryfile.write(summary)
