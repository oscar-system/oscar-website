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

# use the venv defined in .venv
if [ ! -d ".venv" ]; then
    echo "venv directory not found, initializing..."
    python3 -m venv .venv
    echo "done!"
fi
echo "Activating venv..."
source .venv/bin/activate

# install requirements for the python scripts
echo "Installing python pre requisites..."
python3 -m pip install -r etc/requirements.txt

# get tutorial status
echo "Getting tutorial status....."
./etc/tutorial_status.py
echo "Done!"
# get tutorial last modified dates
echo "Getting tutorial last modified dates......."
./etc/update-dates.py
echo "Done!"
# update version info
echo "Getting OSCAR version info......."
./etc/update-latest-release.py
echo "Done!"
# run jekyll
echo "Running jekyl......."
bundle exec jekyll build --config _config.yml,_config_production.yml -d /srv/www/www-mathe-oscar/data/http
