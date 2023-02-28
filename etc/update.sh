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

# run jekyll
bundle exec jekyll build --config _config.yml,_config_production.yml -d /srv/www/www-mathe-oscar/data/http
