"""
Module
------

    vertical.py

Description
-----------

    This module contains functions for vertical interpolation
    applications.

Functions
---------

    vertical(varin, zarr, levs)

        This method interpolates a 3-dimensional variable to specified
        vertical levels.

Requirements
------------

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

- wrf-python; https://github.com/NCAR/wrf-python

Author(s)
---------

    Henry R. Winterbottom; 07 March 2023

History
-------

    2023-03-07: Henry Winterbottom -- Initial implementation.

"""

# ----

# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

# ----

from typing import List

import numpy
from diags.exceptions import InterpError
from utils.logger_interface import Logger
from wrf import interplevel

# ----

# Define all available module properties.
__all__ = ["interp"]

# ----

logger = Logger(caller_name=__name__)

# ----


def interp(varin: numpy.array, zarr: numpy.array, levs: List) -> numpy.array:
    """
    Description
    -----------

    This method interpolates a 3-dimensional variable to specified
    vertical levels.

    Parameters
    ----------

    varin: ``numpy.array``

        A Python numpy.array 3-dimensional variable to be
        interpolated.

    zarr: ``numpy.array``

        A Python numpy.array for the respective vertical level type;
        this array must be of the same dimension as `varin`.

    levs: ``List``

        A Python list of levels to which to interpolate; the units of
        this list must be identical to the units of the `zarr` array.

    Returns
    -------

    varout: ``numpy.array``

        A Python numpy.array variable containing the 3-dimensional
        variable interpolated to the specified vertical levels.

    Raises
    ------

    InterpError:

        - raised if an exception is encountered during the vertical
          interpolation.

    """

    # Interpolate the 3-dimensional variable specified upon input to
    # the specified vertical-type levels.
    try:
        varout = interplevel(varin.T, zarr.T, levs)
    except Exception as errmsg:
        msg = f"The vertical interpolation failed with error {errmsg}. Aborting!!!"
        raise InterpError(msg=msg) from errmsg

    return varout
