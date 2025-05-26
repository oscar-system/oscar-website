#!/usr/bin/env python3

import os

from datetime import datetime
from github import Github, Auth

API_KEY = os.getenv("API_KEY")
if API_KEY == None:
    print("API key was not found! Authentication will fail!\nSet the environment variable API_KEY "
          "to a github access token and try again!\n")
    exit()

auth = Auth.Token(API_KEY)

g = Github(auth=auth)
failed=False

try:
    repo = g.get_repo("oscar-system/Oscar.jl")
    release = repo.get_latest_release()
except Exception as e:
    print(e)
    print("Network access failed!")
    print("Leaving the release file unchanged!")
    exit()

if not failed:
    dt = release.created_at
    version = release.title[1:]

releasestring = f"version: '{version}'\nyear: '{dt.year}'\nmonth: '{dt.month}'\nday: '{dt.day}'\ndate: {dt.date()}\n"

if os.getcwd().split('/')[-1] == 'etc':
    releasefilepath = '../_data/release.yml'
else:
    releasefilepath = "_data/release.yml"

with open(releasefilepath, 'w') as releasefile:
    releasefile.write(releasestring)
