#!/usr/bin/env python3

import os
import sys

from github import Github, Auth

API_KEY = os.getenv("API_KEY")
if API_KEY == None:
    print("API key was not found! Authentication will fail!\nSet the environment variable API_KEY "
          "to a github access token and try again!\n")
    exit()

auth = Auth.Token(API_KEY)

g = Github(auth=auth)

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
    print("\nNetwork access failed, resulting file will be unchanged!")
    exit()

resultstring = ""

for i in jobs:
    if i.name == "Prepare Tests":
        continue
    print(f"Processing {i.name}.....")
    name = i.name.split()[-1][0:-1]
    status = i.conclusion
    resultstring += f"'{name}': '{status}'\n"

datapath = '/'.join(os.path.abspath(sys.argv[0]).split('/')[0:-2])+'/_data'
statusfilepath = f"{datapath}/examples_status.yml"

if len(resultstring) > 0:
    # only update the file if resultstring is not empty
    with open(statusfilepath, 'w') as statusfile:
        statusfile.write(resultstring)
