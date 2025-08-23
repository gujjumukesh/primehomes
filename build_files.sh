#!/bin/bash

# Install build tools, Python development headers, MySQL client libraries
apt-get update && apt-get install -y build-essential python3-dev libmysqlclient-dev

# Install Rust and Cargo
if ! command -v rustc &> /dev/null || ! command -v cargo &> /dev/null; then
    echo "Rust and Cargo not found. Installing..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    # Ensure Cargo is on PATH for subsequent commands by sourcing env and updating PATH
    export PATH="$HOME/.cargo/bin:$PATH"
    source "$HOME/.cargo/env"
else
    echo "Rust and Cargo already installed."
    # Ensure Cargo is on PATH for subsequent commands by sourcing env and updating PATH
    export PATH="$HOME/.cargo/bin:$PATH"
    source "$HOME/.cargo/env"
fi

# Update pip and install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate
