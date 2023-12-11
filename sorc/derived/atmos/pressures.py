"""
Module
------

    pressures.py

Description
-----------

    This module contains various pressure profile computational
    methods.

Functions
---------

    pressure_from_thickness(inputs_obj)

        This function computes the pressure profile using the isobaric
        thickness for the corresponding variable level interfaces; the
        profile is computed by integrating isobaric interface
        thickness from the top of the atmosphere, downward, to the
        surface.

    pressure_to_sealevel(inputs_obj)

        This function reduces the surface pressure array to sea-level
        following Wallace and Hobbs [1977].

Requirements
------------

- metpy; https://unidata.github.io/MetPy/latest/index.html

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 09 March 2023

History
-------

    2023-03-09: Henry Winterbottom -- Initial implementation.

"""

# ----

from types import SimpleNamespace

import numpy
from metpy.calc import altimeter_to_sea_level_pressure as a2slp
from metpy.units import units
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["pressure_from_thickness", "pressure_to_sealevel"]

# ----

logger = Logger(caller_name=__name__)

# ----


async def pressure_from_thickness(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the pressure profile using the isobaric
    thickness for the corresponding variable level interfaces; the
    profile is computed by integrating isobaric interface thickness
    from the top of the atmosphere, downward, to the surface.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing, at minimum, the
        isobaric level interface thicknesses and the surface pressure
        from which pressure profile will be computed.

    Returns
    -------

    pres: ``units.Quantity``

        A Python units.Quantity variable containing the pressure
        profile; units are Pascals.

    """

    # Initialize the pressure profile.
    dpres = numpy.array(varobj.pressure.values)
    pres = dpres
    pres[0, :, :] = numpy.array(varobj.surface_pressure.values)

    # Compute the pressure profile using the surface pressure and
    # layer thickness; proceed accordingly.
    msg = "Computing the pressure profile array."
    logger.info(msg=msg)
    for zlev in range(pres.shape[0] - 2, 0, -1):
        pres[zlev, :, :] = pres[zlev + 1, :, :] + dpres[zlev, :, :]

    return pres


# ----


async def pressure_to_sealevel(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function reduces the surface pressure array to sea-level
    following Wallace and Hobbs [1977].

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing, at minimum, the
        surface pressure, the surface elevation, and the temperature
        profile from which the sea-level pressure will be computed.

    Returns
    -------

    pslp: ``units.Quantity``

        A Python units.Quantity variable containing the surface
        pressure reduced to sea-level.

    """

    # Reduce the surface pressure value to the sea-surface.
    msg = "Computing the pressure reduced to sea-level."
    logger.info(msg=msg)
    pslp = a2slp(
        altimeter_value=varobj.surface_pressure.values[:, :],
        height=varobj.surface_height.values[:, :],
        temperature=varobj.temperature.values[0, :, :],
    )

    return pslp
