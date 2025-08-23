#!/bin/bash

# Install build tools, Python development headers, MySQL client libraries and Python itself
apt-get update && apt-get install -y build-essential python3-dev python3-pip libmysqlclient-dev

# Install Rust and Cargo and ensure it's on PATH for subsequent commands
if ! command -v rustc &> /dev/null || ! command -v cargo &> /dev/null; then
    echo "Rust and Cargo not found. Installing..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Update pip and install Python dependencies
pip install --upgrade pip
# Ensure Rust/Cargo is available for packages that need to compile extensions
RUSTUP_HOME="$HOME/.rustup" CARGO_HOME="$HOME/.cargo" pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
