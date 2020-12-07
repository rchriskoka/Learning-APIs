#!/bin/sh
PIPENV_IGNORE_VIRTUALENVS=1
export FLASK_APP=./cashman/index.py
source $(pipenv --venv)/bin/activate
flask run --host=0.0.0.0
