#!/bin/bash

# Install build tools, Python development headers, MySQL client libraries
apt-get update && apt-get install -y build-essential python3-dev libmysqlclient-dev

# Install Rust and Cargo
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source "$HOME/.cargo/env" # Ensure Cargo is on PATH for subsequent commands

# Update pip and install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
