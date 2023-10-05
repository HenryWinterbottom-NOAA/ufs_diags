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
ENV DIAGS_ROOT="/opt/ufs_diags"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN $(command -v apt-get) update -y && \
    $(command -v apt-get) install -y --no-install-recommends && \
    $(command -v apt-get) install -y gfortran && \
    $(command -v rm) -r -f /var/lib/apt/lists/*
ENV PATH="/opt/miniconda/bin:${PATH}"

RUN $(command -v git) clone --recursive "${UFS_DIAGS_GIT_URL}" --branch "${UFS_DIAGS_GIT_BRANCH}" "${DIAGS_ROOT}" && \
    $(command -v pip) install -r "${DIAGS_ROOT}/requirements.txt" && \
    echo "export DIAGS_ROOT=${DIAGS_ROOT}/sorc/diags" >> /root/.bashrc

ENV PYTHONPATH="${DIAGS_ROOT}/sorc:${PYTHONPATH}"