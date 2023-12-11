"""
Module
------

    ll2ra.py

Description
-----------

    This module contains functions to coordinate transform
    interpolations.

Functions
---------

    ll2ra(varin, lats, lons, lat_0, lon_0, max_radius, drho, dphi)

        This function interpolates a 2-dimensional variable, defined
        on a Cartesian type grid, to a polar projection grid defined
        by the attributes for the polar projection specified upon
        entry.

Requirements
------------

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 07 March 2023

History
-------

    2023-03-07: Henry Winterbottom -- Initial implementation.

"""

# ----

# pylint: disable=invalid-name
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

# ----

from types import SimpleNamespace

import numpy
from grids.haversine import haversine
from scipy.interpolate import griddata
from tools import parser_interface

# ----

# Define all available module properties.
__all__ = ["ll2ra"]

# ----


def ll2ra(
    varin: numpy.array,
    lats: numpy.array,
    lons: numpy.array,
    lat_0: float,
    lon_0: float,
    max_radius: float,
    drho: float,
    dphi: float,
) -> SimpleNamespace:
    """
    Description
    -----------

    This function interpolates a 2-dimensional variable, defined on a
    Cartesian type grid, to a polar projection grid defined by the
    attributes for the polar projection specified upon entry.

    Parameters
    ----------

    varin: ``numpy.array``

        A Python numpy.array variable containing the 2-dimensional
        variable defined along the respective Cartesian grid.

    lats: ``numpy.array``

        A Python numpy.array variable containing the 2-dimensional
        grid of latitude coordinate values; the coordinate values are
        assumed order south to north; units are degrees.

    lons: ``numpy.array``

        A Python numpy.array variable containing the 2-dimensional
        grid of longitude coordinate values; the coordinate values are
        assumed to be within in the range[-180.0 to 180.0]; units are
        degrees.

    lat_0: ``float``

        A Python float value defining the reference latitude
        coordinate value from which the polar grid projection will be
        defined; units are degrees.

    lon_0: ``float``

        A Python float value defining the reference longitude
        coordinate value from which the polar grid projection will be
        defined; the coordinate values are assumed to be within in the
        range[-180.0 to 180.0]; units are degrees;

    max_radius: ``float``

        A Python float value defining the maximum radial distance for
        which to define the polar grid projection; units are meters.

    drho: ``float``

        A Python float variable defining the radial distance interval
        for the polar projection; units are meters.

    dphi: ``float``

        A Python float value defining the aximuthal interval for the
        polar projection; units are degrees.

    Returns
    -------

    varobj: ``SimpleNamespace``

        A Python SimpleNamespace object containing the interpolated
        variable as well as the attributes of the polar projection.

    """

    # Initialize the coordinate arrays.
    varobj = parser_interface.object_define()
    (varobj.lat_0, varobj.lon_0) = (lat_0, lon_0)
    fix = (varobj.lat_0, varobj.lon_0)
    varin = numpy.ravel(varin)
    lats = numpy.ravel(lats)
    lons = numpy.ravel(lons)
    varobj.dphi = numpy.radians(dphi)
    varobj.drho = drho
    varobj.max_radius = max_radius
    varobj.radial = numpy.arange(0.0, (varobj.max_radius + varobj.drho), varobj.drho)
    varobj.azimuth = numpy.arange(
        -1.0 * numpy.pi, (numpy.pi + 2.0 * varobj.dphi), varobj.dphi
    )

    # Compute the radial distance relative to the specified
    # geographical coordinate location.
    rho = numpy.array(
        [haversine(fix, (lats[idx], lons[idx])) for idx in range(len(lats))]
    )
    xx = numpy.array([haversine(fix, (lat_0, lons[idx])) for idx in range(len(lats))])
    xx = numpy.where(lons < lon_0, -1.0 * xx, xx)
    yy = numpy.array([haversine(fix, (lats[idx], lon_0)) for idx in range(len(lats))])
    yy = numpy.where(lats < lat_0, -1.0 * yy, yy)
    phi = numpy.arctan2(yy, xx)

    # Interpolate the variable from the Cartesian projection to the
    # polar projection.
    (r_mesh, theta_mesh) = numpy.meshgrid(varobj.radial, varobj.azimuth)
    var = griddata((rho, phi), varin, (r_mesh, theta_mesh), method="linear").ravel()
    interp_var = numpy.array(var)
    check = numpy.logical_not(numpy.isnan(interp_var))
    xp = check.ravel().nonzero()[0]
    fp = interp_var[numpy.logical_not(numpy.isnan(interp_var))]
    x = numpy.isnan(interp_var).ravel().nonzero()[0]
    interp_var[numpy.isnan(var)] = numpy.interp(x, xp, fp)
    (varobj.nrho, varobj.nphi) = [len(varobj.radial), len(varobj.azimuth)]
    varobj.varout = numpy.array(interp_var).reshape((varobj.nphi, varobj.nrho)).T

    return varobj
