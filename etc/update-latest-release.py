#!/usr/bin/env python3

import os

from datetime import datetime
from github import Github, Auth

API_KEY = os.getenv("API_KEY")

auth = Auth.Token(API_KEY)

g = Github(auth=auth)
failed=False

try:
    repo = g.get_repo("oscar-system/Oscar.jl")
    release = repo.get_latest_release()
except Exception as e:
    print(e)
    print("Network access failed! Falling back to default date and version!")
    failed = True
    dt = datetime(1970, 1, 1)
    version = '0.0.0'

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
