#!/usr/bin/env python3

import os
import sys
from datetime import timezone
from github import Github, Auth


def gh_output(**kvs):
    """
    Write simple key=value outputs for GitHub Actions.
    Only used when GITHUB_OUTPUT is set (i.e. in CI).
    """
    path = os.getenv("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        for k, v in kvs.items():
            v = "" if v is None else str(v)
            f.write(f"{k}={v}\n")


API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()
if not API_KEY:
    print(
        "API key was not found! Set API_KEY or GITHUB_TOKEN to a GitHub token.",
        file=sys.stderr,
    )
    gh_output(changed="false", reason="no-token")
    sys.exit(1)

auth = Auth.Token(API_KEY)
g = Github(auth=auth)

TARGET_REPO = os.getenv("TARGET_REPO", "oscar-system/Oscar.jl")
JULIA_MIN = os.getenv("JULIA_MIN", "1.10")

# repo root = parent of this file's directory
ownpath = os.path.abspath(sys.argv[0])
repopath = os.path.dirname(os.path.dirname(ownpath))
datapath = os.path.join(repopath, "_data")
os.makedirs(datapath, exist_ok=True)

releasefilepath = os.path.join(datapath, "release.yml")

try:
    repo = g.get_repo(TARGET_REPO)
    release = repo.get_latest_release()
except Exception as e:
    print(e, file=sys.stderr)
    print("Network access failed! Leaving the release file unchanged!")
    gh_output(changed="false", reason="fetch-failed")
    sys.exit(0)

# Determine version string (strip leading 'v')
tag = release.tag_name or release.name or release.title
version = (tag or "").lstrip("v").strip()

if not version:
    print("Could not determine version from latest release.", file=sys.stderr)
    gh_output(changed="false", reason="no-version")
    sys.exit(0)

dt = release.published_at or release.created_at
if not dt:
    print("Could not determine release date.", file=sys.stderr)
    gh_output(changed="false", reason="no-date")
    sys.exit(0)

dt = dt.replace(tzinfo=timezone.utc)

# Read old version (if file exists) without adding a YAML dependency
old_version = None
if os.path.exists(releasefilepath):
    with open(releasefilepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("version:"):
                # version: "1.2.3"
                _, val = line.split(":", 1)
                old_version = val.strip().strip('"')
                break

if old_version == version:
    print(f"{releasefilepath} already has latest version {version}. Nothing to do.")
    gh_output(
        changed="false",
        reason="up-to-date",
        version=version,
        old_version=old_version or "",
        target_repo=TARGET_REPO,
    )
    sys.exit(0)

# Build new YAML contents
releasestring = f"""version: "{version}"
year: "{dt.year}"
month: "{dt.month}"
day: "{dt.day}"
date: "{dt.date()}"
julia-min: "{JULIA_MIN}"
"""

print(f"releasefilepath is {releasefilepath}")
with open(releasefilepath, "w", encoding="utf-8") as releasefile:
    releasefile.write(releasestring)

print(f"Updated {releasefilepath} to version {version} (was {old_version or 'none'}).")

gh_output(
    changed="true",
    reason="updated",
    version=version,
    old_version=old_version or "",
    published_utc=dt.isoformat(timespec="seconds"),
    target_repo=TARGET_REPO,
)
