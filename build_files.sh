#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install -r requirements.txt # CHANGED

echo "Make Migrations..."
python3 manage.py makemigrations --noinput # CHANGED
python3 manage.py migrate --noinput # CHANGED

echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear # CHANGED