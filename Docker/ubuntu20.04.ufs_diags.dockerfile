# File: Docker/ubuntu20.04.ufs_diags.dockerfile
# Author: Henry R. Winterbottom
# Date: 28 August 2023

# -------------------------
# * * * W A R N I N G * * *
# -------------------------

# It is STRONGLY urged that users do not make modifications below this
# point; changes below are not supported.

# -------------------------
# * * * W A R N I N G * * *
# -------------------------

FROM ghcr.io/henrywinterbottom-noaa/ubuntu20.04.ufs_pyutils:latest
ENV UFS_DIAGS_GIT_URL="https://www.github.com/HenryWinterbottom-NOAA/ufs_diags.git"
ENV UFS_DIAGS_GIT_BRANCH="develop"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN $(command -v apt-get) update -y && \
    $(command -v apt-get) install -y --no-install-recommends && \
    $(command -v apt-get) install -y gfortran && \
    $(command -v rm) -r -f /var/lib/apt/lists/*
ENV PATH="/miniconda/bin:${PATH}"

RUN $(command -v git) clone --recursive "${UFS_DIAGS_GIT_URL}" --branch "${UFS_DIAGS_GIT_BRANCH}" /opt/ufs_diags && \
    cd /opt/ufs_diags && \
    $(command -v pip) install -r /opt/ufs_diags/requirements.txt
ENV PYTHONPATH="/opt/ufs_diags/sorc:${PYTHONPATH}"