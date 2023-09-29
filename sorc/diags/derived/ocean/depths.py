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

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 27 September 2023

History
-------

    2023-09-27: Henry Winterbottom -- Initial implementation.

"""

# ----

from types import SimpleNamespace

import numpy
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["depth_from_profile"]

# ----

logger = Logger(caller_name=__name__)

# ----


def depth_from_profile(varobj: SimpleNamespace) -> numpy.array:
    """
    Description
    -----------

    This function defines a 3-dimensional grid of depth values from a
    single column array of depth values.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing, at minimum, the
        2-dimensional latitude and longitude arrays and the
        1-dimensional depth profile array from the the 3-dimensional
        grid will be defined.

    Returns
    -------

    depth: numpy.array

        A Python numpy.array variable containing a 3-dimensional grid
        of depth values.

    """

    # Initialize and define the depth grid.
    msg = "Defining depth grid from depth profile array."
    logger.info(msg=msg)
    depth = numpy.zeros((len(varobj.depth_profile.values),
                        len(varobj.latitude.values[:, 0]),
                        len(varobj.longitude.values[0, :])
                         ))
    depth = numpy.tile(varobj.depth_profile.values,
                       (depth.shape[2], depth.shape[1], 1)).T

    return depth
