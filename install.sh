#!/usr/bin/env bash

# File: install.sh
# Author: Henry R. Winterbottom
# Date: 12 December 2023

# Description: This script installs the dependencies for the
#   `ufs_diags` package and establishes the run-time environment
#   configuration.

# Usage: ./install

# Imported Environment Variables

# INSTALL_PATH: The directory tree path to the `ufs_diags` GitHub
#   clone; if not specified this defaults to `${PWD}`.

# ----

# Configure the run-time environment.
set -x -e

export INSTALL_PATH=${INSTALL_PATH:-"${PWD}"}

echo "Installing in path ${INSTALL_PATH}"
$(command -v pip) install --upgrade pip
$(command -v pip) install -r "${INSTALL_PATH}/dependencies/ufs_pyutils/requirements.txt"
