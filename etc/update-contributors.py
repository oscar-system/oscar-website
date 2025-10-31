#!/usr/bin/env python3
import os
import json
import yaml
import requests
import subprocess

def custom_sort_function(item):
    name, _ = item
    sortweight = {"name": 0, "affiliation": 1, "email": 2, "github": 3, "website": 4,
                  "paid_by_dfg": 5,"status": 6, "comment": 7, "aka": 8, "aka_email": 9,
                  "repos": 10}
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

for i in peopleList:
    if 'repos' not in i.keys():
        i['repos'] = []

names = [i['github'] for i in peopleList if 'github' in i]
repoList = ["thofma/Hecke.jl", "oscar-system/Oscar.jl", "Nemocas/Nemo.jl",
            "Nemocas/AbstractAlgebra.jl", "oscar-system/GAP.jl", "oscar-system/Polymake.jl",
            "oscar-system/Singular.jl", "algebraic-solving/AlgebraicSolving.jl"]

newList = []
newCoauthorList = []
namelist = []
newpersonlist = []
github_newusers = []
github_userlist = []
github_username = '__notfound__'
API_KEY = (os.getenv("API_KEY") or os.getenv("GITHUB_TOKEN") or "").strip()
summarystring = ""
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
    gitlog = subprocess.Popen(['git', 'shortlog', '-se', '--since=1 year ago', '--group=author', '--group=trailer:co-authored-by'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = gitlog.communicate()
    dnamelist = []
    for line in output.decode().strip().split("\n"):
        # line format: "  42  My Name <mymail@example.com>"
        parts = line.strip().split("\t")
        if len(parts) < 2:
            continue
        name_email = parts[-1]
        if "<" in name_email and ">" in name_email:
            name = name_email.split("<")[0].strip()
            email = name_email.split("<")[1].split(">")[0].strip()
            dnamelist.append([name, email])
    print(dnamelist)

    namelist.extend(dnamelist)
    count = 0
    for i in dnamelist:
        count = count+1
        print(f"Item {count} of {len(dnamelist)}...")
        print(i)
        if i[0] == 'dependabot[bot]':
            print("Skipping dependabot!")
            continue
        if "[bot]" in i[0]:
            print(f"Skipping suspected bot {i[0]}")
            continue
        email = i[1]
        process = subprocess.run(['git', 'log', f'--author={email}', '--format=%H', '-n 1'],
                                   capture_output=True)
        hash = process.stdout.decode().strip()
        github_commit_url = f"https://api.github.com/repos/{repo}/commits/{hash}"
        #ask github API for username
        r = requests.get(github_commit_url, headers={"Authorization":f"Bearer {API_KEY}"})
        if r.status_code == 200:
            j = json.loads(r.text)
            github_username = '__notfound__'
            if j['author'] == None:
                # this commit was authored by someone and committed by someone else
                # so github can't find a github user for the author, only for committed
                # so we go through our list entire people list and see if we know the combination of
                # name and email already
                # or if the name exists in an aka
                # or if the email exists in aka_email
                flag = False
                for person in peopleList:
                    if 'email' in person.keys() and 'name' in person.keys():
                        if i[0] == person['name'] and i[1] == person['email']:
                            # we know the person, check if we know the github ID
                            if 'github' in person.keys() and person['github'] != '':
                                # we know the person and the github, just mark person as active
                                github_username = person['github']
                                flag = True
                                break
                        elif "aka" in person:
                            # the person has an alias
                            if i[0] in person["aka"]:
                                if 'github' in person.keys() and person['github'] != '':
                                    # we know the person and the github, just mark person as active
                                    github_username = person['github']
                                    flag = True
                                    break
                        elif "aka_email" in person:
                            # the person has an alias email
                            if i[1] in person["aka_email"]:
                                if 'github' in person.keys() and person['github'] != '':
                                    # we know the person and the github, just mark person as active
                                    github_username = person['github']
                                    flag = True
                                    break
                if not flag:
                    summarystring += f"- Github username not found for {i[0]} with email {i[1]}. Excluding from people_list.yml\n"
                    continue
            if github_username == '__notfound__':
                github_username = j['author']['login']
        elif github_commit_url == f"https://api.github.com/repos/{repo}/commits/":
            # this is a case of a co-author
            flag = False
            for person in peopleList:
                if 'email' in person.keys() and 'name' in person.keys():
                    if i[0] == person['name'] and i[1] == person['email']:
                            flag = True
                            break
                    elif "aka" in person:
                        # the person has an alias
                        if i[0] in person["aka"]:
                            if 'github' in person.keys() and person['github'] != '':
                                # we know the person and the github, just mark person as active
                                github_username = person['github']
                                flag = True
                                break
                    elif "aka_email" in person:
                        # the person has an alias email
                        if i[1] in person["aka_email"]:
                            if 'github' in person.keys() and person['github'] != '':
                                # we know the person and the github, just mark person as active
                                github_username = person['github']
                                flag = True
                                break
                    elif i[0] == person['name'] or i[1] == person['email']:
                        github_username = person['github']
                        flag = True
                        break
            if not flag:
                # a co author we don't know about at all
                gitlog = subprocess.Popen(['git', 'shortlog', '--format="%h %s %(trailers:key=Co-authored-by)"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                gitcommit = subprocess.Popen(['grep', i[0]], stdin=gitlog.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output = gitcommit.communicate()[0].decode()
                output = output.strip().strip('"').split()[0]
                newCoauthorList.append([i[0], i[1], repo, output])
        else:
            # this will never happen, except if the API lies to you
            # or blocks access
            print(r.status_code)
            print(r)
            print(r.text)
            print(email)
            print(github_commit_url)
            github_username = "__notfound__"
            flag = False

        assert github_username != "__notfound__"
        if github_username not in names and github_username not in github_newusers and github_username != "__notfound__":
            print("A new contributor!")
            newpersonlist.append(i[0])
            print(f"{i[0]}\t{i[1]}\t{github_username}")
            github_newusers.append(github_username)
            newList.append([i[0], i[1], github_username, [repo]])
        elif github_username in names:
            user = [item for item in peopleList if 'github' in item and item['github'] == github_username][0]
            if repo not in user['repos']:
                user['repos'].append(repo)
        else:
            # github_username in github_newusers
            user = [item for item in newList if item[2] == github_username][0]
            if repo not in user[3]:
                user[3].append(repo)
        if github_username not in github_userlist:
            github_userlist.append(github_username)
    os.chdir("..")

# mark active / retired
# if PI, don't touch them
os.chdir("..")
retcount = 0
revcount = 0
retpersonlist = []
revpersonlist = []
for i in peopleList:
    if 'github' not in i:
        #co authors
        continue
    if i['status']=='pi':
        continue
        #don't touch a thing!
    elif i['github'] in github_userlist:
        if i['status'] == 'retired':
            revcount += 1
            revpersonlist.append(i['name'])
        i['status'] = 'active'
    else:
        if i['status'] == 'active':
            retcount += 1
            retpersonlist.append(i['name'])
        i['status'] = 'retired'

np = []
for i in newList:
    if "users.noreply.github.com" in i[1]:
        np.append({"name": i[0], "github": i[2], "status": "active", "repos": i[3]})
        summarystring += f"- Email not found for {i[0]} ({i[2]})..!\n"
    else:
        np.append({"name": i[0], "email": i[1], "github": i[2], "status": "active", "repos": i[3]})
peopleList.extend(np)

np = []
for i in newCoauthorList:
    np.append({"name": i[0], "email": i[1], "status": "active", "comment": f"Co-author of commit {i[3]}","repos": [i[2]]})
peopleList.extend(np)

sortedPeopleList = sorted(peopleList, key= lambda d: d['name'].split()[-1])

# save yml to *NEW* file
# how inefficient is list comprehension ?
pilist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedPeopleList if i['status'] == "pi"]
activelist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedPeopleList if i['status'] == "active"]
retiredlist = [dict(sorted(i.items(), key=custom_sort_function)) for i in sortedPeopleList if i['status'] == "retired"]
with open('../_data/people_list.yml', 'w') as outfile:
    outfile.write("# It is possible that people marked as 'retired' may have the repo key as an "
                  "empty array.\n# This is because people are marked as retired if the update "
                  "script could not find them in any repo.\n# Retired people only have repo "
                  "information if repo information about them was known when they were\n# active "
                  "(or manually added) by a maintainer.\n\n")
    yaml.dump(sortedPeopleList, outfile, Dumper=MyDumper, sort_keys = False, allow_unicode=True)

summarystring = f"""This PR updates the contributors list based on the latest changes.
New contributors : {len(newpersonlist)} | {newpersonlist}
Revived contributors : {revcount} | {revpersonlist}
Newly retired contributors : {retcount} | {retpersonlist}
New co-authors : {len(newCoauthorList)} | {newCoauthorList}
\nSummary Notes:\n\n"""+ summarystring

with open("../summary.txt", 'w') as summaryfile:
    summaryfile.write(summarystring)
