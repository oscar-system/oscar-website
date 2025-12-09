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

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
REPOS_DIR = os.path.join(PROJECT_ROOT, "repos")
CONTRIBUTORS_FILE = os.path.join(PROJECT_ROOT, "_data", "contributors.yml")
SUMMARY_FILE = os.path.join(PROJECT_ROOT, "summary.txt")

# Auth
API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()

# Git config
GIT_LOG_SINCE = "--since=1 year ago"
GIT_LOG_FORMAT_1 = "--format=%aN <%aE>%n%(trailers:unfold,key=Co-authored-by)"
GIT_LOG_FORMAT_2 = (
    "--format=%H %(trailers:only,unfold,separator=|,key=Co-authored-by) %s"
)

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

# Known bot identities that we want to exclude, even if they don't have [bot] in name.
KNOWN_BOT_EMAILS = {"codex@openai.com", "noreply@anthropic.com", "copilot@github.com"}
KNOWN_BOT_NAMES = {"codex", "claude", "copilot", "GitHub Copilot"}

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

YAML_HEADER = (
    "# It is possible that people marked as 'retired' may have the repo key as an empty array.\n"
    "# This is because people are marked as retired if the update script could not find them in "
    "any repo.\n"
    "# Retired people only have repo information if repo information about them was known when "
    "they were\n"
    "# active (or manually added) by a maintainer.\n\n"
)


##########################################
# 2. Globals (runtime state; mutated)
##########################################

current_contributors = []  # loaded from YAML
email_owner = {}  # dict: lowercased email to person dict
name_owner = {}  # dict: normalized name to person dict
aggregate = {}  # list of dicts for all contributors at the time of running this script
summarystring = ""  # intermediate output for information and debugging


##########################################
# All function definitions live here now
##########################################

def norm_name(s: str) -> str:
    # return " ".join((s or "").split()).casefold()
    # if s is empty string, use s as empty string (why the need for this if?)
    # split s into thing separated by space
    # join the separated parts of s by spaces
    # casefold the resulting thing
    # that just means we can s.casefold(), right?
    return s.casefold()


def lookup_user(gh_username: str, email: str, name: str) -> dict | None:
    if gh_username:
        user = name_owner.get(norm_name(gh_username))
    elif email:
        user = email_owner.get(email.casefold())
    else:
        user = name_owner.get(norm_name(name))
    return user

##########################################
# 6. Helpers to find (co)-author details
##########################################


def find_author_github_nick(email: str, repos: list[str]) -> str:
    if not email:
        return ""
    for r in repos:
        commit_hash = git_out(
            full_repo_dir(r),
            "log",
            GIT_LOG_SINCE,
            f"--author={email}",
            "--format=%H",
            "-n",
            "1",
        ).strip()
        if not commit_hash:
            continue
        url = f"https://api.github.com/repos/{r}/commits/{commit_hash}"
        resp = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
        if resp.status_code != 200:
            continue
        author = resp.json().get("author")
        if author and author.get("login"):
            return author["login"]
    return ""


def find_coauthor_commit(name: str, email: str, repos: list[str]) -> str:
    targets = {t for t in (name.casefold(), email.casefold()) if t}
    for r in repos:
        out = git_out(full_repo_dir(r), "log", GIT_LOG_SINCE, GIT_LOG_FORMAT_2)
        for line in out.splitlines():
            low = line.casefold()
            if not any(t in low for t in targets):
                continue
            m = HASH_RE.search(line)
            if m:
                return m.group(0)
    return "(no hash found)"

# find co-authors


suspected_bots = set([])


def process_log_into_aggregate(res: str, repo: str) -> None:
    global summarystring  # , aggregate, suspected_bots # linter complains about aggregate and
                                                        # suspected_bots
    for raw in res.splitlines():
        line = raw.strip()
        if not line:
            continue

        if line.casefold().startswith("co-authored-by:"):
            line = line.split(":", 1)[1].strip()

        low = line.casefold()
        if "[bot]" in low:
            suspected_bots.add((repo, line))
            continue
        if "<" not in line or ">" not in line:
            summarystring += f"- Skipping non-address line in {repo}: {line!r}\n"
            continue

        name, email = parseaddr(line)
        name = " ".join(unicodedata.normalize("NFKC", name).split())
        email = unicodedata.normalize("NFKC", email).strip()
        if not email or not name:
            summarystring += (
                f"- Missing {'email' if not email else 'name'} for {name or email} in {repo}; "
                "skipping\n"
            )
            continue

        if email.casefold() in KNOWN_BOT_EMAILS or norm_name(name) in KNOWN_BOT_NAMES:
            suspected_bots.add((repo, line))
            continue

        owner = email_owner.get(email.casefold()) or name_owner.get(norm_name(name))
        known_github = owner.get("github") if owner else None

        if known_github:
            key = ("gh", known_github.casefold())
        else:
            key = ("email", ((owner and owner.get("email")) or email).casefold())

        rec = aggregate.setdefault(
            key,
            {
                "name": name,
                "email": email,
                "known_github": known_github,
                "repos": set(),
            },
        )
        rec["repos"].add(repo)
        if known_github and not rec["known_github"]:
            rec["known_github"] = known_github
        if (
            "users.noreply.github.com" in rec["email"]
            and "users.noreply.github.com" not in email
        ):
            rec["name"], rec["email"] = name, email


def full_repo_dir(repo_full: str) -> str:
    return os.path.join(REPOS_DIR, repo_full.split("/")[-1])


def git_out(repo_dir: str, *args: str) -> str:
    res = subprocess.run(
        ["git", "-C", repo_dir, *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return res.stdout


##########################################
# 3. Read information from contributors.yml
##########################################


try:
    with open(CONTRIBUTORS_FILE, "r", encoding="utf-8") as ymlfile:
        current_contributors = yaml.safe_load(ymlfile) or []
except FileNotFoundError:
    print(f"Error: Could not find {CONTRIBUTORS_FILE}")
    sys.exit(1)
except yaml.YAMLError as e:
    print(f"Error parsing YAML file {CONTRIBUTORS_FILE}: {e}")
    sys.exit(1)

for person in current_contributors:
    person.setdefault("repos", [])


##########################################
# 4. Build fast alias lookup
##########################################

for p in current_contributors:
    if p.get("email"):
        email_owner[p.get("email").casefold()] = p
    for ae in p.get("aka_email") or ():
        email_owner[ae.casefold()] = p
    if p.get("name"):
        name_owner[norm_name(p.get("name"))] = p
    for an in p.get("aka") or ():
        name_owner[norm_name(an)] = p
    if p.get("github"):
        name_owner[norm_name(p.get("github"))] = p

##########################################
# 5. Find (co)authors of all repos
##########################################

os.makedirs(REPOS_DIR, exist_ok=True)
for repo in REPO_LIST:
    print(f"Processing {repo}...")
    repo_dir = full_repo_dir(repo)
    if not os.path.isdir(repo_dir):
        subprocess.run(
            ["git", "clone", f"https://github.com/{repo}", repo_dir], check=True
        )
    else:
        subprocess.run(["git", "-C", repo_dir, "pull", "--ff-only"], check=True)
    res_stdout = git_out(
        repo_dir, "log", "--use-mailmap", GIT_LOG_SINCE, GIT_LOG_FORMAT_1
    )
    process_log_into_aggregate(res_stdout, repo)


##########################################
# 7. Post-aggregation enrichment & updates
##########################################

prev_status = {id(p): p.get("status") for p in current_contributors}
seen_current = set()
new_names = []
for key, rec in aggregate.items():
    name, email, repos = rec["name"], rec["email"], rec["repos"]
    gh = rec.get("known_github") or find_author_github_nick(email, repos)
    user = lookup_user(gh, email, name)
    if user:  # Existing contributor
        have = set(user["repos"])
        user["repos"].extend(r for r in repos if r not in have)
        if gh and not user.get("github"):
            user["github"] = gh
            name_owner[norm_name(gh)] = user
        seen_current.add(id(user))
    else:  # Brand-new person: add immediately, mark seen, collect name for summary
        newp = {
            "name": name,
            "email": email,
            "repos": sorted(set(repos)),
            "status": "active",
        }
        if gh:
            newp["github"] = gh
            name_owner[norm_name(gh)] = newp
        else:
            newp["comment"] = (
                f"Co-author of commit {find_coauthor_commit(name, email, repos)}"
            )
        current_contributors.append(newp)
        seen_current.add(id(newp))
        new_names.append(name)

for p in current_contributors:
    if p.get("status") == "pi":
        continue
    p["status"] = "active" if id(p) in seen_current else "retired"
    p["repos"] = sorted(set(p["repos"]))


##########################################
# 8. Dump output
##########################################

# Write new content to CONTRIBUTORS_FILE
people_sorted = sorted(
    current_contributors,
    key=lambda d: (d.get("name", "").split()[-1].lower())
)
ordered_people = [
    dict(sorted(p.items(), key=lambda kv: SORT_WEIGHT.get(kv[0], 999)))
    for p in people_sorted
]
with open(CONTRIBUTORS_FILE, "w", encoding="utf-8") as f:
    f.write(YAML_HEADER)
    yaml.dump(ordered_people, f, sort_keys=False, allow_unicode=True)

# Write summary
if len(suspected_bots) > 0:
    bots = sorted({line for _, line in suspected_bots})
    repos = sorted({repo for repo, _ in suspected_bots})
    summarystring += (
        f"- Skipped {len(bots)} bot accounts across {len(repos)} repos:\n"
        + "".join(f"  - {b}\n" for b in bots)
    )
revived_names = [
    p.get("name")
    for p in current_contributors
    if id(p) in seen_current
    and id(p) in prev_status
    and prev_status[id(p)] == "retired"
]
newly_retired_names = [
    p.get("name")
    for p in current_contributors
    if p.get("status") == "retired" and prev_status.get(id(p)) == "active"
]
summary = (
    "This PR updates the contributors list based on the latest changes.\n"
    f"New contributors : {len(new_names)} | {new_names}\n"
    f"Revived contributors : {len(revived_names)} | {revived_names}\n"
    f"Newly retired contributors : {len(newly_retired_names)} | {newly_retired_names}\n\n"
    "Summary Notes:\n\n"
) + summarystring
with open(SUMMARY_FILE, "w", encoding="utf-8") as summaryfile:
    summaryfile.write(summary)
