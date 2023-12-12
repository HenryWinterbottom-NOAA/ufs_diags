# File: Docker/ubuntu20.04.ufs_pyutils.dockerfile
# Author: Henry R. Winterbottom
# Date: 29 August 2023

# -------------------------
# * * * W A R N I N G * * *
# -------------------------

# It is STRONGLY urged that users do not make modifications below this
# point; changes below are not supported.

# -------------------------
# * * * W A R N I N G * * *
# -------------------------

FROM ghcr.io/henrywinterbottom-noaa/ubuntu20.04.miniconda:latest
ENV UFS_PYUTILS_GIT_URL="https://www.github.com/HenryWinterbottom-NOAA/ufs_pyutils.git"
ENV UFS_PYUTILS_GIT_BRANCH="develop"
ENV PYUTILS_ROOT="/opt/ufs_pyutils"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN $(command -v git) clone --recursive "${UFS_PYUTILS_GIT_URL}" --branch "${UFS_PYUTILS_GIT_BRANCH}" "${PYUTILS_ROOT}" && \
    $(command -v pip) install -r "${PYUTILS_ROOT}/requirements.txt" && \
    $(command -v conda) clean --tarballs

ENV PATH="/opt/miniconda/bin:${PATH}"
ENV PYTHONPATH="/opt/ufs_pyutils:${PYTHONPATH}"
