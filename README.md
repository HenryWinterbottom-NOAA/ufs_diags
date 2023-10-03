[![License](https://img.shields.io/badge/License-LGPL_v2.1-black)](https://github.com/HenryWinterbottom-NOAA/ufs_diags/blob/develop/LICENSE)
![Linux](https://img.shields.io/badge/Linux-ubuntu%7Ccentos-lightgrey)
![Python Version](https://img.shields.io/badge/Python-3.5|3.6|3.7-blue)
[![Code style: black](https://img.shields.io/badge/Code%20Style-black-purple.svg)](https://github.com/psf/black)
[![Documentation Status](https://readthedocs.org/projects/ufs-diags/badge/?version=latest)](https://ufs-diags.readthedocs.io/en/latest/?badge=latest)

[![Python Coding Standards](https://github.com/HenryWinterbottom-NOAA/ufs_diags/actions/workflows/pycodestyle.yaml/badge.svg)](https://github.com/HenryWinterbottom-NOAA/ufs_diags/actions/workflows/pycodestyle.yaml)

# Cloning

This repository utilizes several sub-modules from various sources. To
obtain the entire system, do as follows.

~~~shell
user@host:$ git clone --recursive https://github.com/HenryWinterbottom-NOAA/ufs_diags
~~~

# Dependencies

The package dependencies and the respective repository and manual
installation attributes are provided in the table below.

<div align="left">

| Dependency Package | <div align="left">Installation Instructions</div> | 
| :-------------: | :-------------: |
| <div align="left">[`geopy`](https://github.com/geopy/geopy)</div> | <div align="left">`pip install geopy==2.3.0`</div> |
| <div align="left">[`gsw`](https://github.com/TEOS-10/GSW-Python)</div> | <div align="left">`pip install gsw`</div> |
| <div align="left">[`metpy`](https://unidata.github.io/MetPy/latest/index.html)</div> | <div align="left">`pip install metpy==1.4.0`</div> |
| <div align="left">[`pyspharm`](https://github.com/jswhit/pyspharm)</div> | <div align="left">`pip install pyspharm==1.0.9`</div> |
| <div align="left">[`ufs_pyutils`](https://github.com/HenryWinterbottom-NOAA/ufs_pyutils)</div> | <div align="left">`pip install ufs-pyutils`</div> | 
| <div align="left">[`wrf-python`](https://github.com/NCAR/wrf-python)</div> | <div align="left">`pip install wrf-python==1.3.4.1`</div> |

</div>

# Installing Package Dependencies

In order to install the respective Python packages upon which
`ufs_diags` is dependent, do as follows.

~~~shell
user@host:$ cd /path/to/ufs_diags
user@host:$ /path/to/pip install update
user@host:$ /path/to/pip install -r /path/to/ufs_diags/requirements.txt
~~~

For additional information using `pip` and `requirements.txt` type files, see [here](https://pip.pypa.io/en/stable/reference/requirements-file-format/).

# Building and Installing

In order to install via the Python setup applications, do as follows.

~~~shell
user@host:$ cd /path/to/ufs_diags
user@host:$ /path/to/python setup.py build --user
user@host:$ /path/to/python setup.py install --user
~~~

For additional information and options for building Python packages, see [here](https://docs.python.org/3.5/distutils/setupscript.html).

# Docker Containers

Docker containers containing the `ufs_diags` dependencies can be
collected as follows.

~~~shell
user@host:$ /path/to/docker pull ghcr.io/henrywinterbottom-noaa/ubuntu20.04.ufs_diags:latest
~~~

To execute within the Docker container, do as follows.

~~~shell
user@host:$ /path/to/docker run -it ghcr.io/henrywinterbottom-noaa/ubuntu20.04.ufs_diags:latest
~~~

# Forking

If a user wishes to contribute modifications done within their
respective fork(s) to the authoritative repository, we request that
the user first submit an issue and that the fork naming conventions
follow those listed below.

- `docs/user_fork_name`: Documentation additions and/or corrections for the application(s).

- `feature/user_fork_name`: Additions, enhancements, and/or upgrades for the application(s).

- `fix/user_fork_name`: Bug-type fixes for the application(s) that do not require immediate attention.

- `hotfix/user_fork_name`: Bug-type fixes which require immediate attention to fix issues that compromise the integrity of the respective application(s). 
