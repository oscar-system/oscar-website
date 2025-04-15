#!/usr/bin/env python

import os
from github import Github, Auth

API_KEY = os.getenv("API_KEY")

auth = Auth.Token(API_KEY)

g = Github(auth=auth)
failed=False

try:
    # anything that calls out to a network, and might face a transient error
    repo = g.get_repo("oscar-system/TutorialTesterforOscar")
    workflow = repo.get_workflow("CI.yml")
    run = workflow.get_runs()[0]    # get most recent run
    jobs = run.jobs()
except Exception as e:
    print(e)
    falied = True

resultstring = ""

if not failed:
    # if failed, resultstring remains empty, and all tutorials are marked as "out of date"
    # is this a good idea? maybe we should assume everything is current if we can't tell for sure?
    for i in jobs:
        if i.name == "Prepare Tests":
            continue
        name = i.name.split()[-1][0:-1]
        status = i.conclusion
        resultstring += f"{name}: {status}\n"

if os.getcwd().split('/')[-1] == 'etc':
    statusfilepath = "../_data/examples_status"
else:
    statusfilepath = "_data/examples_status"

with open(statusfilepath, 'w') as statusfile:
    statusfile.write(resultstring)
