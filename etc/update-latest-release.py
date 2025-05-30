#!/usr/bin/env python3

import os
import sys

from datetime import datetime
from github import Github, Auth

API_KEY = os.getenv("API_KEY")
if API_KEY == None:
    print("API key was not found! Authentication will fail!\nSet the environment variable API_KEY "
          "to a github access token and try again!\n")
    exit()

auth = Auth.Token(API_KEY)

g = Github(auth=auth)

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

releasestring = f"version: '{version}'\nyear: '{dt.year}'\nmonth: '{dt.month}'\nday: '{dt.day}'\ndate: {dt.date()}\n"

datapath = '/'.join(os.path.abspath(sys.argv[0]).split('/')[0:-2])+'/_data'
releasefilepath = f"{datapath}/release.yml"

print(f"releasefilepath is {releasefilepath}")

with open(releasefilepath, 'w') as releasefile:
    releasefile.write(releasestring)
