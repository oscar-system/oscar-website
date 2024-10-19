#!/bin/sh
set -e

# fetch latest changes
cd /srv/www/www-mathe-oscar/data/oscar-website/
git fetch --all --prune
git checkout --force gh-pages
git reset --hard origin/gh-pages

# add webhook secret
cat /srv/www/www-mathe-oscar/data/webhook.secret >> .htaccess

# install gems
bundle config set --local path 'vendor/bundle'
bundle install

# get tutorial status
statusurl=$(curl -SsL --retry 5 "https://api.github.com/repos/oscar-system/TutorialTesterforOscar/actions/workflows/CI.yml/runs?per_page=1" | jq  '.workflow_runs[0].jobs_url' | sed 's/"//g')
curl -SsL --retry 5 $statusurl | jq '.["jobs"][1:] | .[] | .name+":"+.conclusion' | sed 's/^.*\s.*\s.*\s//' | sed 's/):/: /' | sed s'/"$//' > _data/examples_status.yml
# get tutorial last modified dates
cd etc
python3 update-dates.py
# update contributors list
python3 update-contributors.py
cd ..
# run jekyll
bundle exec jekyll build --config _config.yml,_config_production.yml -d /srv/www/www-mathe-oscar/data/http
