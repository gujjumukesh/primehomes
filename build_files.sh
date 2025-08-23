#!/bin/bash

# Install build tools, Python development headers, MySQL client libraries, Python 3.11, and pkg-config
apt-get update && apt-get install -y build-essential python3.11-dev python3.11-pip libmysqlclient-dev pkg-config

# Set Python 3.11 as the default for the build environment
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Rust toolchain verification and installation
if ! command -v rustc &> /dev/null || ! command -v cargo &> /dev/null; then
    echo "Rust and Cargo not found. Installing..."
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --no-modify-path
    export PATH="$HOME/.cargo/bin:$PATH"
    echo "Rust and Cargo installed successfully."
else
    echo "Rust and Cargo already installed. Verifying and updating toolchain..."
    rustup update
    export PATH="$HOME/.cargo/bin:$PATH"
    echo "Rust toolchain verified and updated."
fi

# Update pip and install Python dependencies with extended timeout
echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing Python dependencies..."
# Ensure Rust/Cargo is available for packages that need to compile extensions
RUSTUP_HOME="$HOME/.rustup" CARGO_HOME="$HOME/.cargo" pip install --timeout=600 -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

echo "Build script finished successfully."
