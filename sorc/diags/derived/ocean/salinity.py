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
        practical salinity and returns a units.Quantity containing the
        respective values and attributes; the following are the
        mandatory computed/defined variables within the
        SimpleNamespace object `varobj` upon entry:

        - latitude; the geographical coordinate latitude array.

        - longitude; the geographical coordinate longitude array.

        - salinity; the practical salinity array.

        - seawater_pressure; the sea-water pressure array.

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

import gc
from types import SimpleNamespace

import numpy
from diags.derived.derived import check_mandvars
from gsw import SA_from_SP
from metpy.units import units
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["absolute_from_practical"]

# ----

logger = Logger(caller_name=__name__)

# ----


def absolute_from_practical(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the absolute salinity from the practical
    salinity and returns a units.Quantity containing the respective
    values and attributes; the following are the mandatory
    computed/defined variables within the SimpleNamespace object
    `varobj` upon entry:

    - latitude; the geographical coordinate latitude array.

    - longitude; the geographical coordinate longitude array.

    - salinity; the practical salinity array.

    - seawater_pressure; the sea-water pressure array.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    abs_sal: units.Quantity

        A Python units.Quantity variable containing the 3-dimensional
        absolute salinity array.

    """

    # Compute the absolute salinity from the practical salinity.
    msg = "Computing absolute salinity."
    logger.warn(msg=msg)
    check_mandvars(
        varobj=varobj,
        varlist=["latitude", "longitude", "salinity", "seawater_pressure"],
    )
    abs_sal = numpy.zeros(numpy.shape(varobj.salinity.values.magnitude))
    for idx in range(numpy.shape(varobj.salinity.values.magnitude)[0]):
        msg = (
            f"Computing absolute salinity for level {(idx+1)} of "
            f"{numpy.shape(varobj.salinity.values.magnitude)[0]}."
        )
        logger.info(msg=msg)
        abs_sal[idx, ...] = SA_from_SP(
            SP=varobj.salinity.values.magnitude[idx, ...],
            p=varobj.seawater_pressure.values.magnitude[idx, ...],
            lat=varobj.latitude.values.magnitude,
            lon=varobj.longitude.values.magnitude,
        )
        gc.collect()
    abs_sal = units.Quantity(abs_sal, "g/kg")
    gc.collect()

    return abs_sal
