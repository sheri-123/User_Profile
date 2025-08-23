#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Upgrade pip and install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear