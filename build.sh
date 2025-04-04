#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your project
pip install django

# Run migrations
python manage.py migrate