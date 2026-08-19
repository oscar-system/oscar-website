#!/usr/bin/env python3

import os
import sys
from datetime import datetime

import yaml
from github import Github, Auth
API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()
if not API_KEY:
    print(
        "API key was not found! Authentication will fail!\n"
        "Set the environment variable API_KEY or GITHUB_TOKEN "
        "to a GitHub access token and try again!\n"
    )
    sys.exit(1)


# Constants
auth = Auth.Token(API_KEY)
g = Github(auth=auth)
ownpath = os.path.abspath(sys.argv[0])
repopath = os.path.dirname(os.path.dirname(ownpath))
datapath = os.path.join(repopath, "_data")
tutorials_path = os.path.join(datapath, "tutorials.yml")


# Read _data/tutorials.yml
with open(tutorials_path, "r", encoding="utf-8") as f:
    tutorials = yaml.safe_load(f)


# Fetch latest last_modified for each tutorial
for tutorial in tutorials:
    try:
        reponame = tutorial["repository"]
        branch = tutorial.get("branch", "master")
        filepath = f"{tutorial['filename']}.ipynb"
        print(f"Getting {reponame}/{filepath} on branch {branch}...")
        repo = g.get_repo(reponame)
        commits = repo.get_commits(path=filepath, sha=branch)
        commit = commits[0]
        dt = commit.commit.committer.date
    except Exception as e:
        print(e)
        print("Using fallback default date for the tutorial.")
        dt = datetime(1970, 1, 1)
    tutorial["last_modified"] = dt.date().strftime("%B %d, %Y")


# Fetch latest test_status for each tutorial
try:
    print("Trying to get jobs...")
    repo = g.get_repo("oscar-system/TutorialTesterforOscar")
    workflow = repo.get_workflow("CI.yml")
    run = workflow.get_runs()[0]  # most recent run
    jobs = run.jobs()
    print("Done!")
except Exception as e:
    print(e)
    print("\nNetwork access failed, resulting file will be unchanged!")
    sys.exit(1)

status_by_name = {}
for job in jobs:
    if job.name == "Prepare Tests":
        continue
    name = job.name.split()[-1][0:-1]
    status = job.conclusion
    if status is None:
        continue
    status_by_name[name] = status


# Update tutorials with their latest test status
for tutorial in tutorials:
    filename = tutorial.get("filename")
    if filename in status_by_name:
        tutorial["test_status"] = status_by_name[filename]


# Write information to file
with open(tutorials_path, "w", encoding="utf-8") as outfile:
    yaml.safe_dump(
        tutorials,
        outfile,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )
