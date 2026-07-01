#!/usr/bin/env python3

# pylint: disable=missing-module-docstring,missing-function-docstring

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

# Known bot identities that we want to exclude, even if they don't have [bot] in name.
KNOWN_BOT_EMAILS = {
    "codex@openai.com",
    "noreply@anthropic.com",
    "copilot@github.com",
    "noreply@chatgpt.com"
}
KNOWN_BOT_NAMES = {
    "codex",
    "claude",
    "copilot",
    "GitHub Copilot",
    "ChatGPT (OpenAI GPT-5.5)"
}

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
    """# It is possible that people marked as 'retired' may have the repo key as an empty array.
# This is because people are marked as retired if the update script could not find them in any repo.
# Retired people only have repo information if repo information about them was known when they were
# active (or manually added) by a maintainer.

"""
)


##########################################
# 2. Globals (runtime state; mutated)
##########################################

email_owner = {}            # dict: lowercased email to person dict
name_owner = {}             # dict: normalized name to person dict
aggregate = {}              # list of dicts for all contributors at the time of running this script


##########################################
# All function definitions live here now
##########################################

##########################################
# 3. Helpers to find (co)-author details
##########################################


def norm(s: str) -> str:
    # return " ".join((s or "").split()).casefold()
    # if s is empty string, use s as empty string (why the need for this if?)
    # split s into thing separated by space
    # join the separated parts of s by spaces
    # casefold the resulting thing
    # that just means we can s.casefold(), right?
    return s.casefold()


def lookup_user(gh_username: str, email: str, name: str) -> dict | None:
    if gh_username:
        user = name_owner.get(norm(gh_username))
    elif email:
        user = email_owner.get(norm(email))
    else:
        user = name_owner.get(norm(name))
    return user


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


def full_repo_dir(repo_full: str) -> str:
    return os.path.join(REPOS_DIR, repo_full.split("/")[-1])


# helpers to find co authors


def find_github_username(email: str, repos: list[str]) -> str:
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
        resp = requests.get(
            url,
            headers={"Authorization": f"Bearer {API_KEY}"},
            timeout=30,
        )
        if resp.status_code != 200:
            print(f"Warning: GitHub API request failed for {url}: {resp.status_code}")
            continue
        author = resp.json().get("author")
        if author and author.get("login"):
            return author["login"]
    return ""


def find_coauthor_commit(name: str, email: str, repos: list[str]) -> str:
    targets = {t for t in (norm(name), norm(email)) if t}
    for r in repos:
        out = git_out(full_repo_dir(r), "log", GIT_LOG_SINCE, GIT_LOG_FORMAT_2)
        for line in out.splitlines():
            low = norm(line)
            if not any(t in low for t in targets):
                continue
            m = HASH_RE.search(line)
            if m:
                return m.group(0)
    print("Warning! No commit hash found for :")
    print("================================")
    print(repos)
    print(name)
    print(email)
    print("================================")
    return "(no hash found)"


# find co-authors


suspected_bots = set([])


def process_log_into_aggregate(res: str, repo: str, summary_string: str) -> None:
    for raw in res.splitlines():
        line = raw.strip()
        if not line:
            continue

        if norm(line).startswith("co-authored-by:"):
            line = line.split(":", 1)[1].strip()

        low = norm(line)
        if "[bot]" in low:
            suspected_bots.add((repo, line))
            continue
        if "<" not in line or ">" not in line:
            summary_string += f"- Skipping non-address line in {repo}: {line!r}\n"
            continue

        name, email = parseaddr(line)
        name = " ".join(unicodedata.normalize("NFKC", name).split())
        email = unicodedata.normalize("NFKC", email).strip()
        if not email or not name:
            summary_string += (
                f"- Missing {'email' if not email else 'name'} for {name or email} in {repo}; "
                "skipping\n"
            )
            continue

        if norm(email) in KNOWN_BOT_EMAILS or norm(name) in KNOWN_BOT_NAMES:
            suspected_bots.add((repo, line))
            continue

        owner = email_owner.get(norm(email)) or name_owner.get(norm(name))
        known_github = owner.get("github") if owner else None

        if known_github:
            key = ("gh", norm(known_github))
        else:
            key = ("email", norm((owner and owner.get("email")) or email))

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


##########################################
# 3. Read information from people_list.yml
##########################################
def main():
    summary_string = ""
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
            email_owner[norm(p.get("email"))] = p
        for ae in p.get("aka_email") or ():
            email_owner[norm(ae)] = p
        if p.get("name"):
            name_owner[norm(p.get("name"))] = p
        for an in p.get("aka") or ():
            name_owner[norm(an)] = p
        if p.get("github"):
            name_owner[norm(p.get("github"))] = p

    ##########################################
    # 5. Find (co)authors of all repos
    ##########################################

    os.makedirs(REPOS_DIR, exist_ok=True)
    for repository in REPO_LIST:
        print(f"Processing {repository}...")
        local_repo_dir = full_repo_dir(repository)
        if not os.path.isdir(local_repo_dir):
            subprocess.run(
                ["git", "clone", f"https://github.com/{repository}", local_repo_dir], check=True
            )
        else:
            subprocess.run(["git", "-C", local_repo_dir, "pull", "--ff-only"], check=True)
        res_stdout = git_out(
            local_repo_dir, "log", "--use-mailmap", GIT_LOG_SINCE, GIT_LOG_FORMAT_1
        )
        process_log_into_aggregate(res_stdout, repository, summary_string)


    ##########################################
    # 7. Post-aggregation enrichment & updates
    ##########################################

    prev_status = {id(p): p.get("status") for p in current_contributors}
    seen_current = set()
    new_names = []
    for _, aggregate_record in aggregate.items():
        contributor_name = aggregate_record["name"]
        contributor_email = aggregate_record["email"]
        contributor_repos = aggregate_record["repos"]
        gh = aggregate_record.get("known_github") or find_github_username(
            contributor_email, contributor_repos
        )
        matched_user = lookup_user(gh, contributor_email, contributor_name)
        if matched_user:  # Existing contributor
            have = set(matched_user["repos"])
            matched_user["repos"].extend(r for r in contributor_repos if r not in have)
            if gh and not matched_user.get("github"):
                matched_user["github"] = gh
                name_owner[norm(gh)] = matched_user
            seen_current.add(id(matched_user))
        else:  # Brand-new person: add immediately, mark seen, collect name for summary
            newp = {
                "name": contributor_name,
                "email": contributor_email,
                "repos": sorted(set(contributor_repos)),
                "status": "active",
            }
            if gh:
                newp["github"] = gh
                name_owner[norm(gh)] = newp
            else:
                newp["comment"] = "Co-author of commit " + \
                    find_coauthor_commit(
                        contributor_name,
                        contributor_email,
                        contributor_repos
                    )
            current_contributors.append(newp)
            seen_current.add(id(newp))
            new_names.append(contributor_name)

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
        bot_repos = sorted({repo for repo, _ in suspected_bots})
        summary_string += f"- Skipped {len(bots)} bot accounts across {len(bot_repos)} repos:\n"
        summary_string += "".join(f"  - {b}\n" for b in bots)

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
        f"""This PR updates the contributors list based on the latest changes.
New contributors : {len(new_names)} | {new_names}
Revived contributors : {len(revived_names)} | {revived_names}
Newly retired contributors : {len(newly_retired_names)} | {newly_retired_names}


Summary Notes:


{summary_string}
"""
    )

    with open(SUMMARY_FILE, "w", encoding="utf-8") as summaryfile:
        summaryfile.write(summary)

if __name__ == "__main__" :
    main()
