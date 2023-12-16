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

    seawater_from_depth(varobj)

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

    2023-09-27: Henry Winterbottom -- Initial implementation.

"""

# ----

from types import SimpleNamespace

from diags.units import mks_units
from gsw import p_from_z
from metpy.units import units
from tools import parser_interface
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["seawater_from_depth"]

# ----

logger = Logger(caller_name=__name__)

# ----


@mks_units
async def seawater_from_depth(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the absolute sea-water pressure profile as
    a function of depth and latitude.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    pres: ``units.Quantity``

        A Python units.Quantity variable containing the 3-dimensional
        absolute sea-water pressure array; units are ``dbar``.

    """

    # Compute the pressure profile as a function of depth.
    msg = "Computing the sea-water pressure from depth."
    logger.info(msg=msg)
    presdict = {
        "depth": units.Quantity(varobj.depth.values, "m").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
    }
    presobj = parser_interface.dict_toobject(in_dict=presdict)
    pres = units.Quantity(p_from_z(z=-1.0 * presobj.depth, lat=presobj.lats), "dbar")

    return pres
