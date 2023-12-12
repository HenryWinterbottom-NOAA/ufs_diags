"""
Module
------

    moisture.py

Description
-----------

    This module contains various moisture variable computation
    methods.

Functions
---------

    spfh_to_mxrt(inputs_obj)

        This function computes the mixing ratio from the specific
        humidity.

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

from metpy.calc import mixing_ratio_from_specific_humidity as mxrt_from_spfh
from metpy.units import units
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["spfh_to_mxrt"]

# ----

logger = Logger(caller_name=__name__)

# ----


async def spfh_to_mxrt(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function computes the mixing ratio from the specific
    humidity.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing, at minimum, the
        specific humidity profile (`specific_humidity`) from which the
        mixing ratio will be computed.

    Returns
    -------

    mxrt: ``units.Quantity``

        A Python units.Quantity variable containing the mixing-ratio
        profile.

    """

    # Compute the mixing ratio profile from the specific humidity
    # profile.
    msg = (
        "Computing the mixing ratio array of dimension "
        f"{varobj.specific_humidity.values.shape}."
    )
    logger.info(msg=msg)
    mxrt = mxrt_from_spfh(specific_humidity=varobj.specific_humidity.values)

    return mxrt
