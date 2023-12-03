"""
Module
------

    depths.py

Description
-----------

    This module contains functions to compute oceanic depth profiles.

Functions
---------

    depth_from_profile(varobj)

        This function defines a 3-dimensional grid of depth values
        from a single column array of depth values.

Requirements
------------

- metpy; https://unidata.github.io/MetPy/latest/index.html

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 27 September 2023

History
-------

    2023-09-27: Henry Winterbottom -- Initial implementation.

"""

# ----

# pylint: disable=invalid-name
# pylint: disable=unused-variable

# ----

from types import SimpleNamespace

import numpy
from metpy.units import units
from tools import parser_interface
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["depth_from_profile"]

# ----

logger = Logger(caller_name=__name__)

# ----


async def depth_from_profile(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function defines a 3-dimensional grid of depth values from a
    single column array of depth values.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the absolute salinity will be computed/defined.

    Returns
    -------

    depth: units.Quantity

        A Python units.Quantity variable containing a 3-dimensional
        grid of depth values; units are ``m``.

    """

    # Initialize and define the depth grid.
    msg = "Defining depth grid from depth profile array."
    logger.info(msg=msg)
    depthdict = {
        "z": units.Quantity(varobj.depth_profile.values, "m").magnitude,
        "lons": units.Quantity(varobj.longitude.values, "degree").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
    }
    depthobj = parser_interface.dict_toobject(in_dict=depthdict)
    nx = len(depthobj.lons[0, :])
    ny = len(depthobj.lats[:, 0])
    nz = len(depthobj.z)
    depth = units.Quantity(numpy.tile(depthobj.z, (nx, ny, 1)).T, "m")

    return depth
