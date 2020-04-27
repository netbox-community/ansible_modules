#!/usr/bin/env bash

# Usage: ./hacking/black.sh

# Run black to reformat all python code
black . --exclude "ansible_collections|venv"
