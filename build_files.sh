#!/bin/bash

# Build the project
echo "Building the project..."

# Install dependencies
pip3 install -r requirements.txt

# Collect static files
python3 -m django collectstatic --noinput --clear --settings=trydjango.settings