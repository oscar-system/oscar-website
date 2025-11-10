#!/usr/bin/env python3

import os
import sys

from datetime import datetime
from github import Github, Auth

API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()
if API_KEY == None:
    print("API key was not found! Authentication will fail!\nSet the environment variable API_KEY "
          "to a github access token and try again!\n")
    exit()

auth = Auth.Token(API_KEY)

g = Github(auth=auth)

ownpath = os.path.abspath(sys.argv[0])
repopath = os.path.dirname(os.path.dirname(ownpath))
datapath = repopath +'/_data'

try:
    repo = g.get_repo("oscar-system/Oscar.jl")
    release = repo.get_latest_release()
except Exception as e:
    print(e)
    print("Network access failed!")
    print("Leaving the release file unchanged!")
    exit()

dt = release.created_at
version = release.title[1:]

releasestring = f"""\
version: "{version}"
year: "{dt.year}"
month: "{dt.month}"
day: "{dt.day}"
date: "{dt.date()}"
julia-min: "1.10"
"""

releasefilepath = f"{datapath}/release.yml"

print(f"releasefilepath is {releasefilepath}")

with open(releasefilepath, 'w') as releasefile:
    releasefile.write(releasestring)
