"""
Module
------

    pressures.py

Description
-----------

    This module contains functions to compute sea-water pressure
    profiles.

Functions
---------

    pressure_from_depth(varobj)

        This function computes the absolute sea-water pressure profile
        as a function of depth and latitude.

Requirements
------------

- gsw; https://www.teos-10.org/pubs/gsw/html/gsw_contents.html

- metpy; https://unidata.github.io/MetPy/latest/index.html

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 27 September 2023

History
-------

    2023-03-09: Henry Winterbottom -- Initial implementation.

"""

from types import SimpleNamespace

import numpy
from gsw import p_from_z
from metpy.units import units
from utils.logger_interface import Logger
from tools import parser_interface
from diags.derived.derived import Derived

# ----

# Define all available module properties.
__all__ = ["pressure_from_depth"]

# ----

logger = Logger(caller_name=__name__)

# ----


def absolute_pressure_from_seawater_pressure(varobj: SimpleNamespace) -> numpy.array:
    """ """


# ----

def seawater_pressure_from_depth(varobj: SimpleNamespace) -> numpy.array:
    """
    Description
    -----------

    This function computes the absolute sea-water pressure profile as
    a function of depth and latitude.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing, at minimum, the
        3-dimensional depth array and the 2-dimensionl latitude array.

    Returns
    -------

    pressure: numpy.array

        A Python numpy.array variable containing the 3-dimensional
        grid of absolute sea-water pressure.

    """

    # Compute the pressure profile as a function of depth.
    msg = "Computing the sea-water pressure from depth and latitude."
    logger.info(msg=msg)
    constants_obj = Derived().constants_obj
    prsunits = parser_interface.object_getattr(
        object_in=units, key=varobj.seawater_pressure.units)
    depth = -1.0*varobj.depth.values.magnitude
    lat = varobj.latitude.values.magnitude
    pressure = (units.Quantity(
        p_from_z(z=depth, lat=lat), "dbar")).to(prsunits)

    return pressure
