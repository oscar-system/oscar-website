import json
import yaml
import requests

from datetime import datetime

ogfile = yaml.safe_load(open("../_data/examples.yml"))

for i in range(len(ogfile)):
    #assemble URL
    repo = f"{ogfile[i]['repository']}"
    filepath = f"{ogfile[i]['filename']}.ipynb"
    url = f'https://api.github.com/repos/{repo}/commits?path={filepath}'

    try:
        #make request
        #unauth API is rate limited at 60 per hour
        #this should be okay for running script once per hour (we have less than 60 tutorials)
        #auth API usage has limit of 5,000 requests per hour.
        r = requests.get(url)
        if r.status_code != 200:
            raise ValueError(f"Reponse must have code 200, we got {r.status_code}")
        r = json.loads(r.content)
    except Exception as e:
        print(e)
        print(f"Got an error {e}.\nContinuing without updating time for {ogfile[i]['filename']}...")
        continue

    #update times
    dt = datetime.strptime(r[0]['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ")
    d = dt.date().strftime("%B %d, %Y")
    ogfile[i]['date'] = d

with open('../_data/examples_with_updated_last_modified.yml', 'w') as outfile:
    outfile.write(yaml.dump(ogfile))
