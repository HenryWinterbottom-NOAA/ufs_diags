UFS Diagnostics Toolbox
=======================

Description
-----------

Python-based diagnostic tools for UFS-based applications.

- **Derived Quantities**: Atmosphere and ocean analysis derived quantities.
- **Grid Diagnostics**: Tools to compute grid-related attributes.
- **Interpolation**: Interpolation applications.
- **Transform Applications**: Mathematical variable transform tools.

Developers
----------

* Henry R. Winterbottom - henry.winterbottom@noaa.gov

Cloning
-------

The ``ufs_diags`` repository can be obtained as follows:

.. code-block:: bash

   user@host:$ /path/to/git clone --recursive https://www.github.com/HenryWinterbottom-NOAA/ufs_diags ./ufs_diags

Dependencies
------------

A Fortran compiler is required for the respective Python dependencies. This package has only been tested against GNU (e.g., ``gfortran``). The following table lists the ``ufs_diags`` Python dependencies.

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - **Package**
     - **Description**
     - **Installation Instructions**
   * - ``geopy``
     - `Python geocoding library <https://github.com/geopy/geopy>`_
     - ``pip install geopy==2.3.0``
   * - ``gsw``
     - `Gibbs SeaWater (GSW) Oceanographic Toolbox <https://www.teos-10.org/pubs/gsw/html/gsw_contents.html>`_
     - ``pip install gsw``
   * - ``metpy``
     - `Weather data tools <https://github.com/Unidata/MetPy>`_
     - ``pip install metpy``
   * - ``pyspharm``
     - `Python spherical harmonics package <https://github.com/jswhit/pyspharm>`_
     - ``pip install pyspharm==1.0.9``
   * - ``wrf-python``
     - `WRF-ARW diagnostics and interpolation routines <https://github.com/NCAR/wrf-python>`_
     - ``pip install wrf-python==1.3.4.1``

The above packages can be installed as follows:

.. code-block:: bash

   user@host:$ cd /path/to/ufs_diags
   user@host:$ /path/to/pip install --upgrade pip
   user@host:$ /path/to/pip install -r requirements.txt

For additional information and options for building Python packages, see `here <https://docs.python.org/3.5/distutils/setupscript.html)>`_.

Virtual Environment
-------------------

Virtual environments can be configured as follows:

.. code-block:: bash

   user@host:$ cd /path/to/ufs_diags/venv
   user@host:$ ./install.sh

The above will configure the virtual environment. To execute applications within the virtual environment, do as follows:

.. code-block:: bash

   user@host:$ cd /path/to/ufs_diags/venv
   user@host:$ ./setup.sh

The above will launch the respective virtual environment.

Container Environments
----------------------

A Docker container environment, supporting and within which the ``ufs_diags`` applications can be executed, may be obtained and executed as follows:

.. code-block:: bash

   user@host:$ /path/to/docker pull ghcr.io/henrywinterbottom-noaa/ubuntu20.04.ufs_diags:latest
   user@host:$ /path/to/docker container run -it ghcr.io/henrywinterbottom-noaa/ubuntu20.04.ufs_diags:latest

.. toctree::
   :hidden:
   :maxdepth: 2

   derived.rst
   grids.rst
   interp.rst
   transforms.rst
