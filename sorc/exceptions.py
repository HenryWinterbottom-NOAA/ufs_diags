# =========================================================================
# File: sorc/exceptions.py
# Author: Henry R. Winterbottom
# Date: 29 August 2023
# Version: 0.0.1
# License: LGPL v2.1
# =========================================================================

"""
Module
------

    exceptions.py

Description
-----------

    This module loads the exceptions package.

Classes
-------

    AtmosDerivedError(msg)

        This is the base-class for exceptions encountered within the
        derived/atmos modules; it is a sub-class of Error.

    DerivedError(msg)

        This is the base-class for exceptions encountered within the
        derived modules; it is a sub-class of Error.

    GridsError(msg)

        This is the base-class for exceptions encountered within the
        grids modules; it is a sub-class of Error.

    InterpError(msg)

        This is the base-class for exceptions encountered within the
        interp modules; it is a sub-class of Error.

    TransformsError(msg)

        This is the base-class for exceptions encountered within the
        transforms modules; it is a sub-class of Error.

Requirements
------------

- ufs_pytils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 10 June 2023

History
-------

    2023-06-10: Henry Winterbottom -- Initial implementation.

"""

# ----

__author__ = "Henry R. Winterbottom"
__maintainer__ = "Henry R. Winterbottom"
__email__ = "henry.winterbottom@noaa.gov"

# ----

from utils.error_interface import Error

# ----

# Define all available attributes.
__all__ = [
    "AtmosDerivedError",
    "DerivedError",
    "GridsError",
    "InterpError",
    "TransformsError",
]

# ----


class AtmosDerivedError(Error):
    """
    Description
    -----------

    This is the base-class for exceptions encountered within the
    derived/atmos modules; it is a sub-class of Error.

    """


# ----


class DerivedError(Error):
    """
    Description
    -----------

    This is the base-class for exceptions encountered within the
    derived modules; it is a sub-class of Error.

    """


# ----


class GridsError(Error):
    """
    Description
    -----------

    This is the base-class for exceptions encountered within the grids
    modules; it is a sub-class of Error.

    """


# ----


class InterpError(Error):
    """
    Description
    -----------

    This is the base-class for exceptions encountered within the
    interp modules; it is a sub-class of Error.

    """

# ----


class TransformsError(Error):
    """
    Description
    -----------

    This is the base-class for exceptions encountered within the
    transforms modules; it is a sub-class of Error.

    """
