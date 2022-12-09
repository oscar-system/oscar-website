#!/bin/sh
set -e

# fetch latest changes
cd $HOME/oscar-website
git fetch --all --prune
git checkout gh-pages
git reset --hard origin/gh-pages

# install gems
bundle config set --local path 'vendor/bundle'
bundle install

# run jekyll
bundle exec jekyll build --config _config.yml,_config_production.yml -d /srv/www/oscar
