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
cd ..
# update version info
curl -SsL https://api.github.com/repos/oscar-system/Oscar.jl/releases/latest > latest.json
version=$(jq '.["name"]' latest.json | sed 's/v//')
date=$(jq '.["created_at"]' latest.json | cut -c2-11)
year=$(echo $date | tr '-' ' ' | awk '{print $1}')
month=$(echo $date | tr '-' ' ' | awk '{print $2}')
day=$(echo $date | tr '-' ' ' | awk '{print $3}')
echo "version: $version" > _data/release.yml
echo "year: \"$year\"" >> _data/release.yml
echo "month: \"$month\"" >> _data/release.yml
echo "day: \"$day\"" >> _data/release.yml
echo "date: \"$year-$month-$day\"" >> _data/release.yml
rm latest.json
# run jekyll
bundle exec jekyll build --config _config.yml,_config_production.yml -d /srv/www/www-mathe-oscar/data/http
