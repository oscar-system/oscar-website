#!/usr/bin/env python3

import os
import sys
import yaml

from datetime import datetime
from github import Github, Auth

API_KEY = os.getenv("API_KEY")
if API_KEY == None:
    print("API key was not found! Authentication will fail!\nSet the environment variable API_KEY "
          "to a github access token and try again!\n")
    exit()

auth = Auth.Token(API_KEY)

g = Github(auth=auth)

if os.getcwd().split('/')[-1] == 'etc':
    ogfile = yaml.safe_load(open("../_data/examples.yml"))
else:
    ogfile = yaml.safe_load(open("_data/examples.yml"))

for i in range(len(ogfile)):

    try:
        # all network requests are in this try block
        reponame = f"{ogfile[i]['repository']}"
        filepath = f"{ogfile[i]['filename']}.ipynb"
        print(f"Getting {reponame}/{filepath}...")
        repo = g.get_repo(reponame)
        commit = repo.get_commits(path=filepath)[0]
        dt = commit.stats.last_modified_datetime
    except Exception as e:
        print(e)
        print("Network access failed. Using fallback default date for the tutorial.")
        dt = datetime(1970, 1, 1)

    #update times
    d = dt.date().strftime("%B %d, %Y")
    ogfile[i]['date'] = d

datapath = '/'.join(os.path.abspath(sys.argv[0]).split('/')[0:-2])+'/_data'
outfilepath = f"{datapath}/examples_with_updated_last_modified.yml"

with open(outfilepath, 'w') as outfile:
    outfile.write(yaml.dump(ogfile))
