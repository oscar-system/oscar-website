#!/usr/bin/env python3

# Imports
import os
import sys
from datetime import timezone
from github import Github, Auth
import yaml
import tomli
import requests

# Constants
TARGET_REPO = os.getenv("TARGET_REPO", "oscar-system/Oscar.jl")
JULIA_MIN_DEFAULT = "1.10"
OWNPATH = os.path.abspath(sys.argv[0])
REPOPATH = os.path.dirname(os.path.dirname(OWNPATH))
DATAPATH = os.path.join(REPOPATH, "_data")
RELEASEFILEPATH = os.path.join(DATAPATH, "release.yml")

# Get/set API key or raise error
API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()
if not API_KEY:
    print("API key was not found! Set API_KEY or GITHUB_TOKEN to a GitHub token.")
    sys.exit(1)

auth = Auth.Token(API_KEY)
g = Github(auth=auth)

# Fetch release
try:
    repo = g.get_repo(TARGET_REPO)
    release = repo.get_latest_release()
except Exception as e:
    print(e)
    print("Failed to fetch latest release info! Leaving the release file unchanged!")
    sys.exit(1)

# Process release version
tag = release.tag_name
version = (tag or "").strip().lstrip("v")
if not version:
    print("Could not determine version from latest release.")
    sys.exit(1)

# Fetch release date/time
dt = release.published_at
if not dt:
    print("Could not determine release date.")
    sys.exit(1)

dt = dt.replace(tzinfo=timezone.utc)

# Read old version
old_version = None
if os.path.exists(RELEASEFILEPATH):
    with open(RELEASEFILEPATH, "r", encoding="utf-8") as yamlfile:
        data = yaml.safe_load(yamlfile)
        old_version = data['version']
else:
    print(f"Release file not found: {RELEASEFILEPATH}")
    sys.exit(1)

# Early exit in case version hasn't changed
if old_version == version:
    print(f"{RELEASEFILEPATH} already has latest version {version}. Nothing to do.")
    sys.exit(0)

# Grab julia-min version from Project.toml
PROJECT_TOML_URL = \
    f"https://raw.githubusercontent.com/oscar-system/Oscar.jl/refs/tags/v{version}/Project.toml"

try:
    r = requests.get(url=PROJECT_TOML_URL, timeout=60)
    t = tomli.loads(r.content.decode())
    julia_min = t["compat"]["julia"]
except Exception as e:
    print(e)
    print(
        "Unable to fetch Oscar.jl's Project.toml. Using a default julia-min value of ",
        JULIA_MIN_DEFAULT
    )
    julia_min = JULIA_MIN_DEFAULT

# Write new release information and signal changes to github workflow
RELEASESTRING = f"""version: "{version}"
year: "{dt.year}"
month: "{dt.month}"
day: "{dt.day}"
date: "{dt.date()}"
julia-min: "{julia_min}"
"""

print(f"RELEASEFILEPATH is {RELEASEFILEPATH}")

with open(RELEASEFILEPATH, "w", encoding="utf-8") as releasefile:
    releasefile.write(RELEASESTRING)

print(f"Updated {RELEASEFILEPATH} to version {version} (was {old_version or 'none'}).")
