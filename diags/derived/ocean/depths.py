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
        from a single column array of depth values.

    isodepth(varobj,varin,isolev,isointrp,interp_type="linear",
             fill_value=numpy.nan)

        This function interpolates an array of variable values to
        determine the depth of the specified iso-level.

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

# pylint: disable=cell-var-from-loop
# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
# pylint: disable=unused-variable

# ----

from types import SimpleNamespace
from typing import List, Tuple, Union

import numpy
from diags.units import mks_units
from metpy.units import units
from scipy.interpolate import interp1d
from tools import parser_interface
from tools.parser_interface import handler
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["depth_from_profile", "isodepth"]

# ----

logger = Logger(caller_name=__name__)

# ----


@mks_units
async def depth_from_profile(varobj: SimpleNamespace) -> units.Quantity:
    """
    Description
    -----------

    This function defines a 3-dimensional grid of depth values from a
    single column array of depth values.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the variables from
        which the absolute salinity will be computed/defined.

    Returns
    -------

    depth: ``units.Quantity``

        A Python units.Quantity variable containing a 3-dimensional
        grid of depth values; units are `m`.

    """

    # Initialize and define the depth grid.
    msg = "Defining depth grid from depth profile array."
    logger.info(msg=msg)
    depthdict = {
        "z": units.Quantity(varobj.depth_profile.values, "m").magnitude,
        "lons": units.Quantity(varobj.longitude.values, "degree").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
    }
    depthobj = parser_interface.dict_toobject(in_dict=depthdict)
    nx = len(depthobj.lons[0, :])
    ny = len(depthobj.lats[:, 0])
    nz = len(depthobj.z)
    depth = units.Quantity(numpy.tile(depthobj.z, (nx, ny, 1)).T, "m")

    return depth


# ----


async def isodepth(
    varobj: SimpleNamespace,
    varin: numpy.array,
    isolev: float,
    isointrp: List = None,
    interp_type: str = "linear",
    fill_value: Union[str, float] = numpy.nan,
) -> Tuple[numpy.array, List]:
    """
    Description
    -----------

    This function interpolates an array of variable values to
    determine the depth of the specified iso-level.

    Parameters
    ----------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the variables from
        which the absolute salinity will be computed/defined.

    varin: ``numpy.array``

        A Python numpy.array variable containing the field from which
        to derive the interpolated value.

    isolev: ``float``

        A Python float value specifying the iso-level for to compute
        the depth.

    Keywords
    --------

    isointrp: ``Union[None, List]``, optional

        A Python list containing the interpolation function; if
        ``NoneType`` upon entry, the interpolation function will be
        computed prior to the interpolation; if a ``List`` upon entry,
        the interpolation function will not be computed and the
        interpolation will be computed using ``isointrp``.

    interp_type: ``str``, optional

        A Python string supporting the interpolation type;
        https://tinyurl.com/scipy-interp1d for the supported options.

    fill_value: ``array-type``, optional

        A Python string or float value specifying how to handle
        numpy.nan and/or missing values; see
        https://tinyurl.com/scipy-interp1d for the supported options.

    Returns
    -------

    varout: ``numpy.array``

        A Python numpy.array variable containing the variable
        ``varin`` interpolated to the specified iso-level defined by
        ``isolev`.

    Notes
    -----

    - All units and/or unit conversions must be performed within the
      calling routine; this function makes no assumptions regarding a
      quantity's units.

    """

    # Interpolate to compute the iso-level for the respective input
    # variable.
    isodict = {
        "depth": units.Quantity(varobj.depth_profile.values, "m").magnitude,
        "lats": units.Quantity(varobj.latitude.values, "degree").magnitude,
    }

    isoobj = parser_interface.dict_toobject(in_dict=isodict)
    depth = units.Quantity(isoobj.depth, "m").magnitude
    lats = units.Quantity(isoobj.lats, "degree").magnitude
    isovarin = numpy.reshape(varin[...], (len(depth), len(lats.flatten())))
    isovarin = numpy.ma.where(isovarin < isolev, numpy.nan, isovarin)
    idx = [list(range(len(lats.flatten())))]
    isodpth = numpy.zeros(len(lats.flatten()))
    if isointrp is None:
        msg = "Computing the interpolation function."
        logger.info(msg=msg)
        isointrp = numpy.empty_like(idx, dtype=object)
        isointrp = [
            interp1d(isovarin[:, idx], depth, kind=interp_type, fill_value=fill_value)
            for idx in range(len(lats.flatten()))
        ]
    msg = "Interpolating variable to find iso-level value."
    logger.info(msg=msg)
    varout = numpy.array(
        [
            handler(lambda: isointrp[idx](isolev), return_none=True)
            if handler(lambda: isointrp[idx](isolev), return_none=True) is not None
            else numpy.nan
            for idx in range(len(lats.flatten()))
        ]
    )
    varout = numpy.reshape(varout, numpy.shape(lats))

    return (varout, isointrp)
