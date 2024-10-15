#!/usr/bin/env python3
import os
import json
import yaml
import requests
import subprocess

peopleList = yaml.safe_load(open("../_data/people_list.yml"))
names = [i['github'] for i in peopleList]
repoList = ["thofma/hecke.jl", "oscar-system/Oscar.jl", "Nemocas/Nemo.jl",
            "Nemocas/AbstractAlgebra.jl", "oscar-system/GAP.jl", "oscar-system/Polymake.jl",
            "oscar-system/Singular.jl"]

newList = []
namelist = []
github_newusers = []
github_userlist = []
API_KEY = ""
# debug assignments
#repoList = ["Nemocas/AbstractAlgebra.jl"]
#github_userlist = ['aaruni96', 'aaruni96', 'aaruni96', 'antonydellavecchia', 'antonydellavecchia',
#                   'benlorenz', 'fieker', 'joschmitt', 'lgoettgens', 'lkastner', 'lkastner',
#                   'Lax202', 'HereAround', 'HereAround', 'fingolfin', 'StevellM', 'ThomasBreuer',
#                   'thofma']

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
    dnamelist = [[i.split(',')[0], i.split(',')[-1]] for i in output.decode().strip().split('\n')]
    namelist.extend(dnamelist)
#if False:
    count = 0
    for i in dnamelist:
        count = count+1
        print(f"Item {count} of {len(dnamelist)}...")
        print(i)
        email = i[1].lstrip().rstrip()
        process = subprocess.Popen(['git', 'log', f'--author={email}', '--format=%H', '-n 1'], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        hash = stdout.decode().strip()
        github_commit_url = f"https://api.github.com/repos/{repo}/commits/{hash}"
        #ask github API for username
        r = requests.get(github_commit_url, headers={"Authorization":f"Bearer {API_KEY}"})
        if r.status_code == 200:
            j = json.loads(r.text)
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

# save yml to *NEW* file
with open('newpeoplelist.yml', 'w') as file:
    yaml.dump(peopleList, file)

#summary
print("\n\n=======================================")
print("Summary")
print("=======================================")
print("The following new users were found. Please (manually) add them to the People List yaml file:\n\n")
for i in newList:
    print(f"\t{i}")
print("\n\n")
