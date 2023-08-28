# File: Docker/ubuntu20.04.ufs_diags.dockerfile
# Author: Henry R. Winterbottom
# Date: 28 August 2023
# Version: 0.0.1
# License: LGPL v2.1

# This Docker recipe file builds a Docker image containing the
# following packages:

# - `ufs_pyutils`;
# - `ufs_diags`.

# -------------------------
# * * * W A R N I N G * * *
# -------------------------

# It is STRONGLY urged that users do not make modifications below this
# point; changes below are not supported.

# ----

FROM noaaufsrnr/ubuntu20.04.ufs_pyutils:latest
ENV UFS_DIAGS_GIT_URL="https://www.github.com/HenryWinterbottom-NOAA/ufs_diags.git"
ENV UFS_DIAGS_GIT_BRANCH="develop"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN $(which apt-get) update -y && \
    $(which apt-get) install -y --no-install-recommends && \
    $(which apt-get) install -y gfortran && \
    $(which rm) -r -f /var/lib/apt/lists/*
ENV PATH="/miniconda/bin:${PATH}"

RUN $(which git) clone --recursive ${UFS_DIAGS_GIT_URL} --branch ${UFS_DIAGS_GIT_BRANCH} /home/ufs_diags && \
    cd /home/ufs_diags && \
    $(which pip) install -r /home/ufs_diags/requirements.txt
ENV PYTHONPATH="/home/ufs_diags/sorc:${PYTHONPATH}"