# =========================================================================

# Module: grids/haversine.py

# Author: Henry R. Winterbottom

# Email: henry.winterbottom@noaa.gov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the respective public license published by the
# Free Software Foundation and included with the repository within
# which this application is contained.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# =========================================================================

"""
Module
------

    haversine.py

Description
-----------

    This module contains functions to determine geometric distances.

Functions
---------

    haversine(loc1, loc2, radius=R_earth.value)

        This function computes and returns the great-circle (i.e.,
        haversine) between two locations.

Requirements
------------

- astropy; https://github.com/astropy/astropy

- ufs_pytils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 10 June 2023

History
-------

    2023-06-10: Henry Winterbottom -- Initial implementation.

"""

# ----

__author__ = "Henry R. Winterbottom"
__maintainer__ = "Henry R. Winterbottom"
__email__ = "henry.winterbottom@noaa.gov"

# ----

from math import asin, cos, radians, sin, sqrt
from typing import Tuple

from astropy.constants import R_earth
from utils.logger_interface import Logger

# ----

logger = Logger(caller_name=__name__)

# ----


def haversine(loc1: Tuple, loc2: Tuple, radius: float = R_earth.value) -> float:
    """
    Description
    -----------

    This function computes and returns the great-circle (i.e.,
    haversine) between two locations.

    Parameters
    ----------

    loc1: Tuple

        A Python tuple containing the geographical coordinates of
        location 1; format is (lat, lon); units are degrees.

    loc2: Tuple

        A Python tuple containing the geographical coordinates of
        location 2; format is (lat, lon); units are degrees.

    Keywords
    --------

    radius: float, optional

        A Python float value defining the radial distance to be used
        when computing the haversine; units are meters.

    Returns
    -------

    hvsine: float

        A Python float value containing the great-circle distance
        (e.g., haversine) between the two locations defined upon
        entry; units are meters.

    """

    # Define the source and destination geographical locations.
    (lat1, lon1) = loc1
    (lat2, lon2) = loc2
    (lat1, lon1, lat2, lon2) = list(map(radians, [lat1, lon1, lat2, lon2]))

    # Compute the great-circle distance (e.g., haversine).
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    dist = sin(dlat / 2.0) ** 2.0 + cos(lat1) * \
        cos(lat2) * sin(dlon / 2.0) ** 2.0
    hvsine = 2.0 * radius * asin(sqrt(dist))

    return hvsine
