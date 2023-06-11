# =========================================================================

# Docker Recipe File: Docker/ubuntu20.04-miniconda_ufs_pyutils.ufs_anlytools.dockerfile

# Email: henry.winterbottom@noaa.gov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the respective public license published by the
# Free Software Foundation and included with the repository within
# which this application is contained.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# =========================================================================

# Description
# -----------

#    This Docker recipe file builds a Docker image containing the
#    following packages.

#    - Ubuntu 20.08 base Linux image;

#    - Miniconda Python 3.9+ stack;

#    - ufs_pyutils applications;

#    - ufs_anlytools applications.

# Docker Instructions
# -------------------

#    The Docker container image should be built as follows.

#    user@host:$ docker build -f ubuntu20.04-miniconda_ufs_pyutils.ufs_anlytools.dockerfile --tag <DOCKER_LOGIN>/ubuntu20.04-miniconda_ufs_pyutils.ufs_anlytools:<TAG> .

#    user@host:$ docker push <DOCKER LOGIN>/ubuntu20.04-miniconda_ufs_pyutils.ufs_anlytools:<TAG>

#    where <TAG> is the tag identifier/name for the respective image
#    and <DOCKER LOGIN> is the user Docker Hub login name.

# Author(s)
# ---------

#    Henry R. Winterbottom; 11 June 2023 

# History
# -------

#    2023-06-11: Henry R. Winterbottom -- Initial implementation.

# Base Image Attributes
# ---------------------

#    Image and Tag: noaaufsrnr/ubuntu20.04-miniconda-ufs_pyutils:latest

# External Package Dependencies
# -----------------------------

#    miniconda; https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh

#    ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

# Latest Container Image Downloads
# --------------------------------

#    Docker Hub: docker pull noaaufsrnr/ubuntu20.04-miniconda_ufs_pyutils.ufs_anlytools:<TAG>

# ----

FROM noaaufsrnr/ubuntu20.04-miniconda-ufs_pyutils:latest
LABEL noaaufsrnr/ubuntu20.04-miniconda_ufs_pyutils_ufs_anlytools.image.authors="Henry.Winterbottom@noaa.gov"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends && \
    apt-get install -y gfortran && \
    rm -rf /var/lib/apt/lists/*
ENV PATH="/miniconda/bin:${PATH}"

RUN git clone https://github.com/HenryWinterbottom-NOAA/ufs_anlytools /ufs_anlytools && \
    cd /ufs_anlytools && \
    /miniconda/bin/pip install -r /ufs_anlytools/requirements.txt
ENV PYTHONPATH="/ufs_anlytools:${PYTHONPATH}"