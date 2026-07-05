#!/bin/bash
set -euo pipefail
echo "Setting up Backup Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
