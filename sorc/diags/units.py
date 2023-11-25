"""
Module
------

    units.py

Description
-----------

    This module contains functions to convert units to various
    standards.

Functions
---------

    mks_units(func)

        This function is a wrapper function for converting variable
        quantities to `meter-kilogram-second` (MKS) standard units.

Requirements
------------

- ufs_pytils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 24 November 2023

History
-------

    2023-11-24: Henry Winterbottom -- Initial implementation.


"""

# ----

import functools
from types import SimpleNamespace
from typing import Callable, Dict, Tuple

from pint import UnitRegistry
from tools import parser_interface

# ----

UNIT_REG = UnitRegistry()

# ----


def mks_units(func: Callable) -> Callable:
    """
    Description
    -----------

    This function is a wrapper function for converting variable
    quantities to `meter-kilogram-second` (MKS) standard units.

    Parameters
    ----------

    func: Callable

        A Python Callable object containing the function to be
        wrapped.

    Returns
    -------

    wrapped_function: Callable

        A Python Callable object containing the wrapped function.

    """

    @functools.wraps(func)
    def wrapped_function(*args: Tuple, **kwargs: Dict) -> SimpleNamespace:
        """
        Description
        -----------

        This method converts variable quantities from the native units
        to MKS units.

        Other Parameters
        ----------------

        args: Tuple

            A Python tuple containing additional arguments passed to
            the constructor.

        kwargs: Dict

            A Python dictionary containing additional key and value
            pairs to be passed to the constructor.

        Returns
        -------

        varobj: SimpleNamespace

            A Python SimpleNamespace object containing the updated
            respective variable arrays in accordance with the MKS unit
            transforms.

        """

        # Collect the Python SimpleNamespace object containing the
        # native variable quantities.
        varobj = func(*args, **kwargs)
        for var in vars(varobj):
            # Convert the native variable quantities to MKS variable
            # quantities.
            varqnt = parser_interface.object_getattr(
                object_in=varobj, key=var, force=True
            )
            quantity = UNIT_REG.Quantity(varqnt.values, varqnt.units)
            quantity_mks = quantity.to_base_units()
            varobj = parser_interface.object_setattr(
                object_in=varobj, key=var, value=quantity_mks
            )
            varqnt.values = quantity_mks.magnitude
            varqnt.units = quantity_mks.units
            varobj = parser_interface.object_setattr(
                object_in=varobj, key=var, value=varqnt
            )

        return varobj

    return wrapped_function
