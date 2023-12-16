"""
Module
------

    salinity.py

Description
-----------

    This module contains functions to compute sea-water salinity.

Functions
---------

    absolute_from_practical(varobj)

        This function computes the absolute salinity from the
        practical salinity.

Requirements
------------

- gsw; https://www.teos-10.org/pubs/gsw/html/gsw_contents.html

- metpy; https://unidata.github.io/MetPy/latest/index.html

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 02 October 2023

History
-------

    2023-10-02: Henry Winterbottom -- Initial implementation.

"""

from types import SimpleNamespace

from diags.units import mks_units
from gsw import SA_from_SP
from metpy.units import units
from tools import parser_interface
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["absolute_from_practical"]

# ----

logger = Logger(caller_name=__name__)

# ----


@mks_units
async def absolute_from_practical(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the absolute salinity from the practical
    salinity.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    asaln: ``units.Quantity``

        A Python units.Quantity variable containing the 3-dimensional
        absolute salinity array; units are `g/kg`.

    """

    # Compute the absolute salinity from the practical salinity.
    msg = "Computing absolute salinity from practical salinity."
    logger.info(msg=msg)
    asalndict = {
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
        "lons": units.Quantity(varobj.longitude.values, "degree").magnitude,
        "pres": units.Quantity(varobj.seawater_pressure.values, "dbar").magnitude,
        "psaln": units.Quantity(varobj.salinity.values, "dimensionless").magnitude,
    }
    asalnobj = parser_interface.dict_toobject(in_dict=asalndict)
    asaln = units.Quantity(
        SA_from_SP(
            SP=asalnobj.psaln, p=asalnobj.pres, lat=asalnobj.lats, lon=asalnobj.lons
        ),
        "g/kg",
    )

    return asaln
