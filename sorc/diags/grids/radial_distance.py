"""
Module
------

    radial_distance.py

Description
-----------

    This module contains functions to compute distances relative to a
    specified geographical location.

Functions
---------

    radial_distance(refloc, latgrid, longrid, radius=R_earth.value)

        This function computes the radial distance for all
        geographical locations relative to a fixed (e.g., reference)
        location using the Haversine formulation.

Requirements
------------

- astropy; https://github.com/astropy/astropy

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 10 June 2023

History
-------

    2023-06-10: Henry Winterbottom -- Initial implementation.

"""

# ----

# pylint: disable=no-name-in-module

from typing import Tuple

import numpy
from astropy.constants import R_earth
from diags.exceptions import GridsError
from diags.grids.haversine import haversine
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["radial_distance"]

# ----

logger = Logger(caller_name=__name__)

# ----


def radial_distance(
    refloc: Tuple,
    latgrid: numpy.array,
    longrid: numpy.array,
    radius: float = R_earth.value,
) -> numpy.array:
    """
    Description
    -----------

    This function computes the radial distance for all geographical
    locations relative to a fixed (e.g., reference) location using the
    Haversine formulation.

    Parameters
    ----------

    refloc: Tuple

        A Python tuple containing the geographical coordinates for the
        reference location; format is (lat, lon); units are degrees.

    latgrid: numpy.array

        A Python numpy.array 1-dimensional variable containing the
        latitude coordinate values; units are degrees.

    longrid: numpy.array

        A Python numpy.array 1-dimensional variable containing the
        longitude coordinate values; units are degrees.

    Keywords
    --------

    radius: float, optional

        A Python float value defining the radial distance to be used
        when computing the haversine; units are meters.

    Returns
    -------

    raddist: numpy.array

        A Python numpy.array 1-dimensional variable containing the
        radial distances relative to the reference geographical
        location; units are meters.

    Raises
    ------

    GeoMetsError:

        - raised if the either or both the latitude and longitude
          arrays are not 1-dimensional upon entry.

    """

    # Check that the input arrays are a single dimension; proceed
    # accordingly.
    if len(latgrid.shape) > 1 or len(longrid.shape) > 1:
        msg = (
            "The input latitude and longitude arrays must be of 1-dimension; "
            f"received latitude dimension {latgrid.shape} and longitude "
            f"dimension {longrid.shape} upon entry. Aborting!!!"
        )
        raise GridsError(msg=msg)

    # Compute the radial distance array relative to the reference
    # location.
    raddist = numpy.zeros(numpy.shape(latgrid))
    raddist = [
        haversine(refloc, (latgrid[idx], longrid[idx]), radius=radius)
        for idx in range(len(raddist))
    ]

    return raddist
