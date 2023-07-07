#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py populate_database