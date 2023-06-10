# =========================================================================

# Module: grids/bearing_geoloc.py

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

    bearing_geoloc.py

Description
-----------

    This module contains functions to determine locations based on
    heading and distance.

Functions
---------

    bearing_geoloc(loc1, dist, heading)

        This function returns the geographical coordinate location
        compute from a reference geographical location and the
        distance and bearing for the destination location.

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

from math import asin, atan2, cos, sin
from typing import Tuple

import numpy
from astropy.constants import R_earth
from utils.logger_interface import Logger

# ----

logger = Logger(caller_name=__name__)

# ----


def bearing_geoloc(
    loc1: Tuple, dist: float, heading: float, radius: float = R_earth.value
) -> Tuple[float, float]:
    """
    Description
    -----------

    This function returns the geographical coordinate location compute
    from a reference geographical location and the distance and
    bearing for the destination location.

    Parameters
    ----------

    loc1: Tuple

        A Python tuple containing the geographical coordinates of
        location 1; format is (lat, lon); units are degrees.

    dist: float

        A Python float value specifying the distance from the
        reference geographical location to the destination location;
        units are meters.

    heading: float

        A Python float value specifying the heading from the reference
        geographical location to the destination location; units are
        degrees.

    Returns
    -------

    loc2: Tuple

        A Python tuple containing the geographical coordinates of
        destination location; format is (lat, lon); units are degrees.

    """

    # Compute the new latitude and longitude geographical location.
    (lat1, lon1, heading) = [
        numpy.radians(loc1[0]),
        numpy.radians(loc1[1]),
        numpy.radians(heading),
    ]
    lat2 = numpy.degrees(
        asin(
            sin(lat1) * cos(dist / radius)
            + cos(lat1) * sin(dist / radius) * cos(heading)
        )
    )
    lon2 = numpy.degrees(
        lon1
        + atan2(
            sin(heading) * sin(dist / radius) * cos(lat1),
            cos(dist / radius) - sin(lat1) * sin(lat2),
        )
    )

    return (lat2, lon2)
