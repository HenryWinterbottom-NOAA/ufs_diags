"""
Module
------

    depths.py

Description
-----------

    This module contains functions to compute oceanic depth profiles.

Functions
---------

    depth_from_profile(varobj)

        This function defines a 3-dimensional grid of depth values
        from a single column array of depth values; the following are
        the mandatory computed/defined variables within the
        SimpleNamespace object `varobj` upon entry:

        - depth_profile; the 1-dimensional depth profile array.

        - latitude; the geographical coordinate latitude array.

        - longitude; the geographical coordinate longitude array.

Requirements
------------

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

import numpy
from diags.derived.derived import check_mandvars
from metpy.units import units
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["depth_from_profile"]

# ----

logger = Logger(caller_name=__name__)

# ----


async def depth_from_profile(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function defines a 3-dimensional grid of depth values from a
    single column array of depth values; the following are the
    mandatory computed/defined variables within the SimpleNamespace
    object `varobj` upon entry:

    - depth_profile; the 1-dimensional depth profile array.

    - latitude; the geographical coordinate latitude array.

    - longitude; the geographical coordinate longitude array.

    Parameters
    ----------

    varobj: SimpleNamespace

        A Python SimpleNamespace object containing the variables from
        which the absolute salinity will be computed/defined.

    Returns
    -------

    depth: units.Quantity

        A Python units.Quantity variable containing a 3-dimensional
        grid of depth values.

    """

    # Initialize and define the depth grid.
    msg = "Defining depth grid from depth profile array."
    logger.info(msg=msg)
    check_mandvars(varobj=varobj, varlist=["depth_profile", "latitude", "longitude"])
    depth = numpy.zeros(
        (
            len(varobj.depth_profile.values),
            len(varobj.latitude.values[:, 0]),
            len(varobj.longitude.values[0, :]),
        )
    )
    depth = numpy.tile(
        varobj.depth_profile.values, (depth.shape[2], depth.shape[1], 1)
    ).T

    return depth
