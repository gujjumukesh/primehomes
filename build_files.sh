#!/bin/bash

# Install build tools, Python development headers, and MySQL client libraries
apt-get update && apt-get install -y build-essential python3-dev libmysqlclient-dev

# Install mise (if not already present) and use it to install Python 3.10
curl https://mise.run | sh
export PATH="$HOME/.mise/bin:$PATH"
mise use python@3.10

# Install Python dependencies
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
