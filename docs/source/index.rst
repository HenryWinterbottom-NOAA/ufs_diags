#######################
UFS Diagnostics Toolbox
#######################

^^^^^^^^^^^
Description
^^^^^^^^^^^

Python-base diagnostic tools for UFS-based applications.

- **Derived Quantities**: Atmosphere and ocean analysis derived quantities.
- **Grid Diagnostics**: Tools to compute grid-related attributes.
- **Interpolation**: Interpolation applications.
- **Transform Applications**: Mathematical variable transform tools.

^^^^^^^^^^
Developers
^^^^^^^^^^

* Henry R. Winterbottom - henry.winterbottom@noaa.gov
  
^^^^^^^
Cloning
^^^^^^^

The ``ufs_diags`` repository may be obtained as follows.

.. code-block:: bash

   user@host:$ /path/to/git clone --recursive https://www.github.com/HenryWinterbottom-NOAA/ufs_diags ./ufs_diags
   
^^^^^^^^^^^^^^^^^^^^^^
Container Environments
^^^^^^^^^^^^^^^^^^^^^^

A Docker container environment, supporting and within which the
``ufs_diags`` applications can be executed, may be obtained and
executed as follows.

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
