"""
Module
------

    radial.py

Description
-----------

    This module contains function(s) implemented for successive radial
    interval interpolations necessary to estimate variable field
    values in defined/specified data-void regions.

Functions
---------

    interp(interp_obj, method="linear")

        This function provides a successive radial interpolation
        application.

Requirements
------------

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 28 April 2023

History
-------

    2023-04-28: Henry Winterbottom -- Initial implementation.

"""

# ----

# pylint: disable=invalid-name
# pylint: disable=no-member
# pylint: disable=too-many-locals

# ----

from types import SimpleNamespace

import numpy
from diags.exceptions import InterpError
from scipy.interpolate import griddata
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["interp"]

# ----

logger = Logger(caller_name=__name__)

# ----


def interp(interp_obj: SimpleNamespace, method: str = "linear") -> numpy.array:
    """
    Description
    -----------

    This function provides a successive radial interpolation
    application.

    Parameters
    ----------

    interp_obj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the radial
        interpolation attributes.

    Keywords
    --------

    method: ``str``, optional

        A Python string specifying the radial interpolation type; the
        following options are supported.

        - nearest; nearest-neighbor interpolation

        - linear; bi-linear interpolation

        Cubic-spline interpolation methods are also supportted but are
        however not optimal for the respective application.

    Returns
    -------

    interp_var: ``numpy.array``

        A Python numpy.array variable containing the variable field
        with the data-void region, included in the respective variable
        field upon entry, updated via the application within.

    Raises
    ------

    InterpError:

        - raised if an exception is encountered while radially
          interpolating the respective variable.

    """

    # Initialize the grid attributes.
    xgrid = numpy.arange(0, numpy.shape(interp_obj.vararray)[1], 1.0)
    ygrid = numpy.arange(0, numpy.shape(interp_obj.vararray)[0], 1.0)
    (xxgrid, yygrid) = numpy.meshgrid(xgrid, ygrid)
    max_dist = interp_obj.distance
    outer_dist = max_dist
    inner_dist = outer_dist - interp_obj.ddist
    interp_var = interp_obj.vararray

    # Interpolate radially inward to recover the initial
    # missing-datum; proceed accordingly.
    try:
        while inner_dist >= 0.0:
            # Define the values to be used to approximate the missing
            # datum.
            msg = f"Interpolating within range {inner_dist} and {outer_dist}."
            logger.info(msg=msg)

            # Interpolate across the specified radial interval.
            varin = interp_var
            varin = numpy.where((interp_obj.raddist <= inner_dist), numpy.nan, varin)
            mask = numpy.ma.masked_invalid(varin)
            xf = xxgrid[~mask.mask]
            yf = yygrid[~mask.mask]
            invar = varin[~mask.mask]
            interp_var[:, :] = griddata(
                (xf, yf), invar, (xxgrid, yygrid), method=method
            )

            # Update the interpolation interval range.
            outer_dist = inner_dist
            inner_dist = outer_dist - interp_obj.ddist
    except Exception as errmsg:
        msg = (
            f"Interpolation application {__name__} failed with error {errmsg}. "
            "Aborting!!!"
        )
        raise InterpError(msg=msg) from errmsg

    return interp_var
