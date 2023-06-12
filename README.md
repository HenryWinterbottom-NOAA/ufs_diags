[![License](https://img.shields.io/badge/License-LGPL_v2.1-black)](https://github.com/HenryWinterbottom-NOAA/ufs_anlytools/blob/develop/LICENSE)
![Linux](https://img.shields.io/badge/Linux-ubuntu%7Ccentos-lightgrey)
![Python Version](https://img.shields.io/badge/Python-3.5|3.6|3.7-blue)

[![Dependencies](https://img.shields.io/badge/Dependencies-ufs__pyutils-orange)](https://github.com/HenryWinterbottom-NOAA/ufs_pyutils)
[![](https://img.shields.io/badge/metpy-orange)](https://unidata.github.io/MetPy/latest/index.html)
[![](https://img.shields.io/badge/pyspharm-orange)](https://github.com/jswhit/pyspharm)
[![](https://img.shields.io/badge/wrf--python-orange)](https://github.com/NCAR/wrf-python)

[![Python Coding Standards](https://github.com/HenryWinterbottom-NOAA/ufs_anlytools/actions/workflows/pycodestyle.yaml/badge.svg)](https://github.com/HenryWinterbottom-NOAA/ufs_anlytools/actions/workflows/pycodestyle.yaml)
[![Container Builds](https://github.com/HenryWinterbottom-NOAA/ufs_anlytools/actions/workflows/containers.yaml/badge.svg)](https://github.com/HenryWinterbottom-NOAA/ufs_anlytools/actions/workflows/containers.yaml)

# Cloning

This repository utilizes several sub-modules from various sources. To
obtain the entire system, do as follows.

~~~
user@host:$ git clone https://github.com/HenryWinterbottom-NOAA/ufs_anlytools
~~~

# Dependencies

The package dependencies and the respective repository and manual
installation attributes are provided in the table below.

<div align="center">

| Dependency Package | <div align="left">Installation Instructions</div> |
| :-------------: | :-------------: |
| [`geopy`](https://github.com/geopy/geopy) | <div align="left">`pip install geopy==2.3.0`</div> |
| [`metpy`](https://unidata.github.io/MetPy/latest/index.html) | <div align="left">`pip install metpy==1.4.0`</div> |
| [`pyspharm`](https://github.com/jswhit/pyspharm) | <div align="left">`pip install pyspharm==1.0.9`</div> |
| [`ufs_pyutils`](https://github.com/HenryWinterbottom-NOAA/ufs_pyutils) | <div align="left">`pip install git+https://github.com/HenryWinterbottom-NOAA/ufs_pyutils.git`</div> | 
| [`wrf-python`](https://github.com/NCAR/wrf-python) | <div align="left">`pip install wrf-python==1.3.4.1`</div> |

</div>

# Installing Package Dependencies

In order to install the respective Python packages upon which
`ufs_anlytools` is dependent, do as follow.

~~~
user@host:$ cd ufs_anlytools
user@host:$ /path/to/pip install update
user@host:$ /path/to/pip install -r /path/to/ufs_anlytools/requirements.txt
~~~

For additional information using `pip` and `requirements.txt` type files, see [here](https://pip.pypa.io/en/stable/reference/requirements-file-format/).

# Forking

If a user wishes to contribute modifications done within their
respective fork(s) to the authoritative repository, we request that
the user first submit an issue and that the fork naming conventions
follow those listed below.

- `docs/user_branch_name`: Documentation additions and/or corrections for the application(s).

- `feature/user_branch_name`: Additions, enhancements, and/or upgrades for the application(s).

- `fix/user_branch_name`: Bug-type fixes for the application(s) that do not require immediate attention.

- `hotfix/user_branch_name`: Bug-type fixes which require immediate attention to fix issues that compromise the integrity of the respective application(s). 

