# Sane Makefile Preamble from https://tech.davis-hansson.com/p/make/
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >
#/preamble

.PHONY: build
build:
>myurl=$$(curl -Ssl "https://api.github.com/repos/oscar-system/TutorialTesterforOscar/actions/workflows/CI.yml/runs?per_page=1" | jq  '.workflow_runs[0].jobs_url' | sed 's/"//g')
#>echo $$myurl
>curl -SsL $$myurl | jq '.["jobs"][1:] | .[] | .name+":"+.conclusion' | sed 's/^.*\s.*\s.*\s//' | sed 's/):/: /' | sed s'/"$$//' > _data/examples_status.yml
>jekyll