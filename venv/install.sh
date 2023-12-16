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

# Define the environment.
export INSTALL_PATH=${INSTALL_PATH:-"${PWD}/../"}
export VENV_PATH="${INSTALL_PATH}/venv"
export FC=${FC:-$(command -v which) gfortan}

# Install the respective packages.
echo "Installing in path ${INSTALL_PATH}"
$(command -v python3) -m venv .
source "${VENV_PATH}/bin/activate"
$(command -v pip) install --upgrade pip
$(command -v mkdir) -p "${VENV_PATH}/dependencies"
$(command -v git) clone --recursive http://www.github.com/henrywinterbottom-noaa/ufs_pyutils --branch develop "${VENV_PATH}/dependencies/ufs_pyutils"
$(command -v pip) install -r "${VENV_PATH}/dependencies/ufs_pyutils/requirements.txt"
$(command -v pip) install -r "${INSTALL_PATH}/requirements.txt"

# Build the wrapper script for the virtual environment.
echo "Building script ${VENV_PATH}/setup.sh"
cat >> ${VENV_PATH}/setup.sh <<EOF
#!/usr/bin/env bash
export PYTHONPATH="${VENV_PATH}/dependencies/ufs_pyutils:${VENV_PATH}/dependencies/ufs_diags"
EOF
$(command -v chmod) +x "${VENV_PATH}/setup.sh"

