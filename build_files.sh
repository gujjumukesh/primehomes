#!/bin/bash

# Install build tools and Python development headers
apt-get update && apt-get install -y build-essential python3-dev

# Install Python dependencies
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
