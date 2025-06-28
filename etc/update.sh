#!/bin/sh
set -ex

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

# use the venv defined in .venv
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
. .venv/bin/activate

# install requirements for the python scripts
OUTDATED_PACKAGES_LIST=$(pip list --outdated --format json | jq -r '.[].name')
if [ -n "$OUTDATED_PACKAGES_LIST" ]
then
        python3 -m pip install --upgrade $OUTDATED_PACKAGES_LIST
fi
python3 -m pip install --upgrade -r etc/requirements.txt

# get tutorial status
./etc/tutorial_status.py || :
./etc/update-dates.py || :
./etc/update-latest-release.py || :

# run jekyll
bundle exec jekyll build --config _config.yml,_config_production.yml -d /srv/www/www-mathe-oscar/data/http
