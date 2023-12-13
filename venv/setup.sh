#!/usr/bin/env bash

# File: setup.sh
# Author: Henry R. Winterbottom
# Date: 13 December 2023

# Description: This script launches an existing virtual environment
#   configuration.

# Usage: ./setup

# ----

# Configure the run-time environment.
set -x -e

$(command -v bash)
source ./bin/activate
