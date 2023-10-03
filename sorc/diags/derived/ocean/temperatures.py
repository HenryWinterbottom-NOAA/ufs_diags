"""
Module
------

    temperatures.py

Description
-----------

    This module contains functions to compute different sea-water
    temperature-type profiles.

Functions
---------

    conservative_from_potential(varobj)

        This function computes the conservative temperature from
        potential temperature and absolute salinity; the following are
        the mandatory computed/defined variables within the
        SimpleNamespace object `varobj` upon entry:

        - absolute_salinity; the 3-dimensional oceanic
          absolute-salinity array.

        - pottemp; the 3-dimensional oceanic potential-temperature
          array.

    insitu_from_conservative(varobj)

        This function computes the insitu-temperature from
        conservative temperature, absolute salinity, and sea-water
        pressure; the following are the mandatory computed/defined
        variables within the SimpleNamespace object `varobj` upon
        entry:

        - absolute_salinity; the 3-dimensional oceanic
          absolute-salinity array.

        - conservative_temperture; the 3-dimensional oceanic
          conservative temperature array.

        - seawater_pressure; the 3-dimensional ocean sea-water
          pressure array.
        

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

import gc
from types import SimpleNamespace

import numpy
from diags.derived.derived import check_mandvars
from gsw import CT_from_pt, t_from_CT
from metpy.units import units
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["conservative_from_potential", "insitu_from_conservative"]

# ----

logger = Logger(caller_name=__name__)

# ----


def conservative_from_potential(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the conservative temperature from potential
    temperature and absolute salinity; the following are the mandatory
    computed/defined variables within the SimpleNamespace object
    `varobj` upon entry:

    - absolute_salinity; the 3-dimensional oceanic absolute-salinity
      array.

    - pottemp; the 3-dimensional oceanic potential-temperature array.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    cons_temp: units.Quantity

        A Python units.Quantity variable containing the conservative
        temperature profile.

    """

    # Compute the conservative temperature from absolute salinity and
    # potential temperature.
    msg = "Computing conservative temperature."
    logger.warn(msg=msg)
    check_mandvars(varobj=varobj, varlist=["absolute_salinity", "pottemp"])
    cons_temp = numpy.zeros(numpy.shape(varobj.pottemp.values.magnitude))
    for idx in range(numpy.shape(varobj.pottemp.values.magnitude)[0]):
        msg = (
            f"Computing conservative temperature for level {(idx+1)} of "
            f"{numpy.shape(varobj.pottemp.values.magnitude)[0]}."
        )
        logger.info(msg=msg)
        cons_temp[idx, ...] = CT_from_pt(
            SA=varobj.absolute_salinity.values.magnitude[idx, ...],
            pt=varobj.pottemp.values.magnitude[idx, ...],
        )
        gc.collect()
    cons_temp = units.Quantity(cons_temp, "degC")
    gc.collect()

    return cons_temp


# ----


def insitu_from_conservative(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the insitu-temperature from conservative
    temperature, absolute salinity, and sea-water pressure; the
    following are the mandatory computed/defined variables within the
    SimpleNamespace object `varobj` upon entry:

    - absolute_salinity; the 3-dimensional oceanic absolute-salinity
      array.

    - conservative_temperture; the 3-dimensional oceanic conservative
      temperature array.

    - seawater_pressure; the 3-dimensional ocean sea-water pressure
      array.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    insitu_temp: units.Quantity

        A Python units.Quantity variable containing the 3-dimensional
        array of insitu-temperature.

    """

    # Compute the insitu-temperature from conservative temperature.
    msg = "Computing insitu-temperature."
    logger.warn(msg=msg)
    check_mandvars(
        varobj=varobj,
        varlist=["absolute_salinity", "conservative_temperature", "seawater_pressure"],
    )
    insitu_temp = numpy.zeros(
        numpy.shape(varobj.conservative_temperature.values.magnitude)
    )
    for idx in range(numpy.shape(insitu_temp)[0]):
        msg = f"Computing insitu-temperature for level {(idx+1)} of {numpy.shape(insitu_temp)[0]}."
        logger.info(msg=msg)
        insitu_temp[idx, ...] = t_from_CT(
            SA=varobj.absolute_salinity.values.magnitude[idx, ...],
            CT=varobj.conservative_temperature.values.magnitude[idx, ...],
            p=varobj.seawater_pressure.values.magnitude[idx, ...],
        )
        gc.collect()
    insitu_temp = units.Quantity(insitu_temp, "degC")
    gc.collect()

    return insitu_temp
