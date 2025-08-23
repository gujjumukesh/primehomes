#!/bin/bash

# Install build tools, Python development headers, and MySQL client libraries
apt-get update && apt-get install -y build-essential python3-dev libmysqlclient-dev

# Install Python dependencies
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
