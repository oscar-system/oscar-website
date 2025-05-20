#!/usr/bin/env python3

import os
from github import Github, Auth

API_KEY = os.getenv("API_KEY")
if API_KEY == None:
    print("API key was not found! Authentication will fail!\nSet the environment variable API_KEY "
          "to a github access token and try again!\n")

assert API_KEY != None

auth = Auth.Token(API_KEY)

g = Github(auth=auth)
failed=False

try:
    print("Trying to get jobs.......")
    # anything that calls out to a network, and might face a transient error
    repo = g.get_repo("oscar-system/TutorialTesterforOscar")
    workflow = repo.get_workflow("CI.yml")
    run = workflow.get_runs()[0]    # get most recent run
    jobs = run.jobs()
    print("Done!")
except Exception as e:
    print(e)
    falied = True

resultstring = ""

if not failed:
    for i in jobs:
        if i.name == "Prepare Tests":
            continue
        print(f"Fetched {i.name}!")
        name = i.name.split()[-1][0:-1]
        status = i.conclusion
        resultstring += f"{name}: {status}\n"
else:
    print("Network access failed, resulting file will be unchanged!")

if os.getcwd().split('/')[-1] == 'etc':
    statusfilepath = "../_data/examples_status.yml"
else:
    statusfilepath = "_data/examples_status.yml"

if resultstring=="":
    # if resultstring is empty, just use the old data
    with open(statusfilepath, 'w') as statusfile:
        statusfile.write(resultstring)
