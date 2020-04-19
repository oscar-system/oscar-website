#!/bin/sh
set -e

GIT_REPO=$HOME/oscar-website
PUBLIC_WWW=/var/www/oscar-website

# fetch latest changes
cd $GIT_REPO
git fetch --all --prune
git checkout gh-pages
git reset --hard origin/gh-pages

# install prerequsits if necessary
export GEM_HOME=$HOME/gems
export PATH=$GEM_HOME/bin:$PATH
export BUNDLE_GEMFILE=$GIT_REPO/etc/Gemfile
bundle install

# run jekyll
bundle exec jekyll build --config _config.yml,_config_production.yml -d $PUBLIC_WWW
