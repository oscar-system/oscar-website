#!/usr/bin/env python3
import os
import json
import yaml
import requests
import subprocess

def custom_sort_function(item):
    name, _ = item
    sortweight = {"name": 0, "affiliation": 1, "email": 2, "github": 3, "website": 4,
                  "paid_by_dfg": 5,"status": 6, "comment": 7}
    return sortweight[name]

# Hack copied from https://github.com/yaml/pyyaml/issues/127#issuecomment-525800484
class MyDumper(yaml.SafeDumper):
    # HACK: insert blank lines between top-level objects
    # inspired by https://stackoverflow.com/a/44284819/3786245
    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1:
            super().write_line_break()

infile = "../_data/people_list.yml"
with open(infile, "r") as ymlfile:
    peopleList = yaml.safe_load(ymlfile)
names = [i['github'] for i in peopleList]
repoList = ["thofma/Hecke.jl", "oscar-system/Oscar.jl", "Nemocas/Nemo.jl",
            "Nemocas/AbstractAlgebra.jl", "oscar-system/GAP.jl", "oscar-system/Polymake.jl",
            "oscar-system/Singular.jl"]

newList = []
namelist = []
github_newusers = []
github_userlist = []
API_KEY = os.getenv("API_KEY") # TODO: rename to whatever is the right env var
summarystring = "This PR updates the contributors list based on the latest changes.\n"
# grab currently active devs
if not os.path.isdir("repos"):
    os.mkdir("repos")
os.chdir("repos")
for repo in repoList:
    print(f"-------------------------------\nProcessing {repo}...\n-------------------------------")
    print("Fetching updates...")
    # if directory already exists
    if os.path.isdir(repo.split('/')[-1]):
        os.chdir(repo.split('/')[-1])
        subprocess.run(["git", "fetch", "--all"], check=True)
        subprocess.run(["git", "pull"], check=True)
    # if directory needs to be freshly cloned
    else:
        subprocess.run(["git", "clone", f"https://github.com/{repo}"], check=True)
        os.chdir(repo.split('/')[-1])
    print("Generating list of authors active in past year...")
    gitlog = subprocess.Popen(['git', 'log', '--since="1 year ago"', '--format=%aN, %aE'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = subprocess.check_output(['sort', '-u'], stdin=gitlog.stdout)
    gitlog.wait()
    dnamelist = [[i.split(',')[0], i.split(',')[-1].lstrip().rstrip()]
                 for i in output.decode().strip().split('\n')]
    namelist.extend(dnamelist)
    count = 0
    for i in dnamelist:
        count = count+1
        print(f"Item {count} of {len(dnamelist)}...")
        print(i)
        email = i[1]
        process = subprocess.Popen(['git', 'log', f'--author={email}', '--format=%H', '-n 1'],
                                   stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        hash = stdout.decode().strip()
        github_commit_url = f"https://api.github.com/repos/{repo}/commits/{hash}"
        #ask github API for username
        r = requests.get(github_commit_url, headers={"Authorization":f"Bearer {API_KEY}"})
        if r.status_code == 200:
            j = json.loads(r.text)
            if j['author'] == None:
                summarystring += f" - Github username not found for {i[0]} with email {i[1]}. Excluding from people_list.yml\n"
                continue
            github_username = j['author']['login']
        else:
            # this will never happen, except if the API lies to you
            # or blocks access
            print(r.status_code)
            print(r)
            print(r.text)
            print(email)
            print(github_commit_url)
            github_username = "__notfound__"
        assert github_username != "__notfound__"
        if github_username not in names and github_username not in github_newusers:
            print("A new contributor!")
            print(f"{i[0]}\t{i[1]}\t{github_username}")
            github_newusers.append(github_username)
            newList.append([i[0], i[1], github_username])
        github_userlist.append(github_username)
    os.chdir("..")

github_userlist = list(set(github_userlist))

# mark active / retired
# if PI, don't touch them
os.chdir("..")
for i in peopleList:
    if i['status']=='pi':
        continue
        #don't touch a thing!
    elif i['github'] in github_userlist:
        i['status'] = 'active'
    else:
        i['status'] = 'retired'

np = []
for i in newList:
    if "users.noreply.github.com" in i[1]:
        np.append({"name": i[0], "github": i[2], "status": "active"})
    else:
        np.append({"name": i[0], "email": i[1], "github": i[2], "status": "active"})
peopleList.extend(np)

sortedPeopleList = sorted(peopleList, key= lambda d: d['name'].split()[-1])

# save yml to *NEW* file
# how inefficient is list comprehension ?
pilist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedPeopleList if i['status'] == "pi"]
activelist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedPeopleList if i['status'] == "active"]
retiredlist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedPeopleList if i['status'] == "retired"]
with open('../_data/people_list.yml', 'w') as outfile:
    outfile.write("######################\n# Project leads\n######################\n\n")
    yaml.dump(pilist, outfile, Dumper=MyDumper, sort_keys=False, allow_unicode=True)
    outfile.write("\n######################\n# Active contributors\n######################\n\n")
    yaml.dump(activelist, outfile, Dumper=MyDumper, sort_keys=False, allow_unicode=True)
    outfile.write("\n######################\n# Retired contributors\n######################\n\n")
    yaml.dump(retiredlist, outfile, Dumper=MyDumper, sort_keys=False, allow_unicode=True)

with open("../summary.txt", 'w') as summaryfile:
    summaryfile.write(summarystring)
