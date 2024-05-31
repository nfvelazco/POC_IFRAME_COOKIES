#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies
pip install --no-cache-dir -r requirements.txt

# Deactivate the virtual environment
deactivate