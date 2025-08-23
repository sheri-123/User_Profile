#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- START OF VERCEL BUILD DIAGNOSTICS ---"

echo " "
echo "Step 1: Listing the contents of the entire project folder..."
# This will show us if your image files are actually there on the server.
ls -R

echo " "
echo "Step 2: Installing dependencies..."
python3 -m pip install -r requirements.txt

echo " "
echo "Step 3: Running the collectstatic command..."
# This is the command that is failing silently.
python3 manage.py collectstatic --noinput --clear

echo " "
echo "Step 4: Listing the contents of the 'staticfiles' folder AFTER collectstatic..."
# This will show us what was actually collected. If the 'images' folder is missing here, we have found the problem.
ls -R staticfiles

echo " "
echo "--- END OF VERCEL BUILD DIAGNOSTICS ---"