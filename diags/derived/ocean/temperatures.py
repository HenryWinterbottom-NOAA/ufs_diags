"""
Module
------

    temperatures.py

Description
-----------

    This module contains functions to compute different temperature
    related quantities.

Functions
---------

    conservative_from_potential(varobj)

        This function computes the conservative temperature from
        potential temperature.

    insitu_from_conservative(varobj)

        This function computes the insitu-temperature from
        conservative temperature.

Requirements
------------

- gsw; https://www.teos-10.org/pubs/gsw/html/gsw_contents.html

- metpy; https://unidata.github.io/MetPy/latest/index.html

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 03 October 2023

History
-------

    2023-10-03: Henry Winterbottom -- Initial implementation.

"""

from types import SimpleNamespace

from diags.units import mks_units
from gsw import CT_from_pt, SA_from_SP, t_from_CT
from metpy.units import units
from tools import parser_interface
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["conservative_from_potential", "insitu_from_conservative"]

# ----

logger = Logger(caller_name=__name__)

# ----


@mks_units
async def conservative_from_potential(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the conservative temperature from potential
    temperature.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    ctemp: ``units.Quantity``

        A Python units.Quantity variable containing the conservative
        temperature; units `degC`.

    """

    # Compute the conservative temperature from the potential
    # temperature.
    msg = "Computing conservative temperature from potential temperature."
    logger.info(msg=msg)
    ctempdict = {
        "ptemp": units.Quantity(varobj.pottemp.values, "degC").magnitude,
        "pres": units.Quantity(varobj.seawater_pressure.values, "dbar").magnitude,
        "psaln": units.Quantity(varobj.salinity.values, "dimensionless").magnitude,
        "lons": units.Quantity(varobj.longitude.values, "degree").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
    }
    ctempobj = parser_interface.dict_toobject(in_dict=ctempdict)
    asaln = units.Quantity(
        SA_from_SP(
            SP=ctempobj.psaln, p=ctempobj.pres, lon=ctempobj.lons, lat=ctempobj.lats
        ),
        "g/kg",
    ).magnitude
    ctemp = units.Quantity(CT_from_pt(SA=asaln, pt=ctempobj.ptemp), "degC")

    return ctemp


# ----


@mks_units
async def insitu_from_conservative(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the insitu-temperature from conservative
    temperature.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    itemp: ``units.Quantity``

        A Python units.Quantity variable containing the
        insitu-temperature; units `degC`.

    """

    # Compute the insitu-temperature from conservative temperature.
    msg = "Computing insitu-temperature from conservative temperature."
    logger.info(msg=msg)
    itempdict = {
        "ptemp": units.Quantity(varobj.pottemp.values, "degC").magnitude,
        "pres": units.Quantity(varobj.seawater_pressure.values, "dbar").magnitude,
        "psaln": units.Quantity(varobj.salinity.values, "dimensionless").magnitude,
        "lons": units.Quantity(varobj.longitude.values, "degree").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
    }
    itempobj = parser_interface.dict_toobject(in_dict=itempdict)
    asaln = units.Quantity(
        SA_from_SP(
            SP=itempobj.psaln, p=itempobj.pres, lon=itempobj.lons, lat=itempobj.lats
        ),
        "g/kg",
    ).magnitude
    ctemp = units.Quantity(CT_from_pt(SA=asaln, pt=itempobj.ptemp), "degC").magnitude
    itemp = units.Quantity(t_from_CT(SA=asaln, CT=ctemp, p=itempobj.pres), "degC")

    return itemp
