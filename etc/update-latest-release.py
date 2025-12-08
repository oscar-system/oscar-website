#!/usr/bin/env python3

# 1. Imports
import os
import sys
from datetime import timezone
from github import Github, Auth
import yaml


# 2. Constants
TARGET_REPO = os.getenv("TARGET_REPO", "oscar-system/Oscar.jl")
JULIA_MIN_DEFAULT = "1.10"
OWNPATH = os.path.abspath(sys.argv[0])
REPOPATH = os.path.dirname(os.path.dirname(OWNPATH))
DATAPATH = os.path.join(REPOPATH, "_data")
RELEASEFILEPATH = os.path.join(DATAPATH, "release.yml")

# 3. Function to write simple key=value outputs for GitHub Actions.
def gh_output(**kvs):
    path = os.getenv("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        for k, v in kvs.items():
            v = "" if v is None else str(v)
            f.write(f"{k}={v}\n")


# 4. Get/set API key or raise error
API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()
if not API_KEY:
    print("API key was not found! Set API_KEY or GITHUB_TOKEN to a GitHub token.")
    gh_output(changed="false", reason="no-token")
    sys.exit(1)
auth = Auth.Token(API_KEY)
g = Github(auth=auth)


# 5. Fetch release
try:
    repo = g.get_repo(TARGET_REPO)
    release = repo.get_latest_release()
except Exception as e:
    print(e)
    print("Network access failed! Leaving the release file unchanged!")
    gh_output(changed="false", reason="fetch-failed")
    sys.exit(1)


# 6. Process release version
tag = release.tag_name
version = (tag or "").strip().lstrip("v")
if not version:
    print("Could not determine version from latest release.")
    gh_output(changed="false", reason="no-version")
    sys.exit(1)


# 7. Fetch release date/time
dt = release.published_at
if not dt:
    print("Could not determine release date.")
    gh_output(changed="false", reason="no-date")
    sys.exit(1)
dt = dt.replace(tzinfo=timezone.utc)


# 8. Read old version
old_version = None
if os.path.exists(RELEASEFILEPATH):
    with open(RELEASEFILEPATH, "r", encoding="utf-8") as yamlfile:
        data = yaml.safe_load(yamlfile)
        old_version = data['version']
else:
    print(f"Release file not found: {RELEASEFILEPATH}")
    sys.exit(1)


# 9. Early exist in case old version and new version agree
if old_version == version:
    print(f"{RELEASEFILEPATH} already has latest version {version}. Nothing to do.")
    gh_output(
        changed="false",
        reason="up-to-date",
        version=version,
        old_version=old_version or "",
        target_repo=TARGET_REPO,
    )
    sys.exit(0)


# Write new release information and signal changes to github workflow
RELEASESTRING = f"""version: "{version}"
year: "{dt.year}"
month: "{dt.month}"
day: "{dt.day}"
date: "{dt.date()}"
julia-min: "{JULIA_MIN}"
"""

print(f"RELEASEFILEPATH is {RELEASEFILEPATH}")

with open(RELEASEFILEPATH, "w", encoding="utf-8") as releasefile:
    releasefile.write(RELEASESTRING)

print(f"Updated {RELEASEFILEPATH} to version {version} (was {old_version or 'none'}).")

gh_output(
    changed="true",
    reason="updated",
    version=version,
    old_version=old_version or "",
    published_utc=dt.isoformat(timespec="seconds"),
    target_repo=TARGET_REPO,
)
