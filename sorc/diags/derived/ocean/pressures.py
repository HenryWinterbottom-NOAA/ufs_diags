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
        as a function of depth and latitude; the following are the
        mandatory computed/defined variables within the
        SimpleNamespace object `varobj` upon entry:

        - depth; the 3-dimensional oceanic depth array.

        - latitude; the geographical coordinate latitude array.

        - seawater_pressure; the sea-water pressure array.

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

import gc
from types import SimpleNamespace

import numpy
from diags.derived.derived import check_mandvars
from gsw import p_from_z
from metpy.units import units
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["seawater_from_depth"]

# ----

logger = Logger(caller_name=__name__)

# ----


def seawater_from_depth(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the absolute sea-water pressure profile as
    a function of depth and latitude; the following are the mandatory
    computed/defined variables within the SimpleNamespace object
    `varobj` upon entry:

    - depth; the 3-dimensional oceanic depth array.

    - latitude; the geographical coordinate latitude array.

    - seawater_pressure; the sea-water pressure array.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the diagnostic variables will be computed/defined.

    Returns
    -------

    sw_pres: units.Quantity

        A Python units.Quantity variable containing the 3-dimensional
        absolute sea-water pressure array.

    """

    # Compute the pressure profile as a function of depth.
    msg = "Computing the sea-water pressure."
    logger.warn(msg=msg)
    check_mandvars(varobj=varobj, varlist=["depth", "latitude"])
    sw_pres = numpy.zeros(numpy.shape(varobj.depth.values.magnitude))
    for idx in range(numpy.shape(sw_pres)[0]):
        msg = (
            f"Computing sea-water pressure from depth for level {(idx+1)} "
            f"of {numpy.shape(sw_pres)[0]}."
        )
        logger.info(msg=msg)
        sw_pres[idx, ...] = p_from_z(
            z=(-1.0 * varobj.depth.values.magnitude)[idx, ...],
            lat=varobj.latitude.values.magnitude,
        )
        gc.collect()
    sw_pres = units.Quantity(sw_pres, "dbar")
    gc.collect()

    return sw_pres
