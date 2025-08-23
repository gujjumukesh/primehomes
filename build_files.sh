#!/bin/bash

# Install build tools, Python development headers, MySQL client libraries, Rust, and Cargo
apt-get update && apt-get install -y build-essential python3-dev libmysqlclient-dev
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$HOME/.cargo/bin:$PATH"

# Install Python dependencies
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
