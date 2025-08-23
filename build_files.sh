#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Upgrade pip and install dependencies
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Apply database migrations
echo "Applying database migrations..."
python3 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear