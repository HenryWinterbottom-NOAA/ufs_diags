"""
Module
------

    heatcontent.py

Description
-----------

    This module contains functions to compute heat-content related
    quantities.

Functions
---------

    specific_heat_capacity(varobj)

        This function computes the specific heat capacity of seawater.

    total_heat_content(varobj)

        This function computes the integrated total ocean heat using
        the specific volume anomaly and the specific heat capacity.

Requirements
------------

- gsw; https://www.teos-10.org/pubs/gsw/html/gsw_contents.html

- metpy; https://unidata.github.io/MetPy/latest/index.html

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 02 December 2023

History
-------

    2023-12-02: Henry Winterbottom -- Initial implementation.

"""

# ----

# pylint: disable=fixme

# ----

from types import SimpleNamespace

import numpy
from diags.derived.ocean.salinity import absolute_from_practical
from diags.derived.ocean.temperatures import (
    conservative_from_potential,
    insitu_from_conservative,
)
from diags.units import mks_units
from gsw import cp_t_exact, specvol_anom_standard
from metpy.units import units
from tools import parser_interface
from utils.logger_interface import Logger

# ----

# Define all available module properties
__all__ = ["specific_heat_capacity", "total_heat_content"]

# ----

logger = Logger(caller_name=__name__)

# ----


@mks_units
async def specific_heat_capacity(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the specific heat capacity of seawater.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    shc: units.Quantity

        A Python units.Quantity variable containing the specific heat
        capacity of seawater; units ``joule/kg*K``.

    """

    # Compute the specific heat capacity of seawater.
    msg = "Computing the specific heat capacity of sea water."
    logger.warn(msg=msg)
    cpdict = {
        "ptemp": units.Quantity(varobj.pottemp.values, "degC").magnitude,
        "lons": units.Quantity(varobj.longitude.values, "degree").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
        "pres": units.Quantity(varobj.seawater_pressure.values, "dbar").magnitude,
        "psaln": units.Quantity(varobj.salinity.values, "dimensionless").magnitude,
    }
    cpobj = parser_interface.dict_toobject(in_dict=cpdict)
    asaln = units.Quantity(
        await absolute_from_practical(varobj=varobj), "g/kg"
    ).magnitude
    itemp = units.Quantity(
        await insitu_from_conservative(varobj=varobj), "degC"
    ).magnitude
    shc = units.Quantity(cp_t_exact(SA=asaln, t=itemp, p=cpobj.pres), "joule/(kg*K)")

    return shc


# ----


@mks_units
async def total_heat_content(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the integrated total ocean heat using the
    specific volume anomaly and the specific heat capacity.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    toch: units.Quantity

        A Python units.Quantity variable containing the total ocean
        heat content; units are ``joule*m^3/kg^2``.

    """

    # Compute the total heat content.
    msg = "Computing the integrated ocean heat content."
    logger.warn(msg=msg)
    ohcdict = {
        "ptemp": units.Quantity(varobj.pottemp.values, "degC").magnitude,
        "lons": units.Quantity(varobj.longitude.values, "degree").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
        "pres": units.Quantity(varobj.seawater_pressure.values, "dbar").magnitude,
        "psaln": units.Quantity(varobj.salinity.values, "dimensionless").magnitude,
    }
    ohcobj = parser_interface.dict_toobject(in_dict=ohcdict)
    asaln = units.Quantity(
        await absolute_from_practical(varobj=varobj), "g/kg"
    ).magnitude
    itemp = units.Quantity(
        await insitu_from_conservative(varobj=varobj), "degC"
    ).magnitude
    ctemp = units.Quantity(
        await conservative_from_potential(varobj=varobj), "degC"
    ).magnitude
    svas = units.Quantity(
        numpy.trapz(
            specvol_anom_standard(SA=asaln, CT=ctemp, p=ohcobj.pres),
            x=ohcobj.pres,
            axis=0,
        ),
        "m^3/kg",
    )
    shc = units.Quantity(await specific_heat_capacity(varobj=varobj), "joule/(kg*K)")
    sumitemp = units.Quantity((itemp[-1, ...] - itemp[0, ...]), "K")
    tohc = svas * shc * sumitemp

    return tohc
