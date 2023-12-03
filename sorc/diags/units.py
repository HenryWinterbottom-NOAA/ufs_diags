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

# ----

# Define all available module properties.
__all__ = ["mks_units"]

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
    async def wrapped_function(*args: Tuple, **kwargs: Dict) -> SimpleNamespace:
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

        varobj: SimpleNamespace # TODO

            A Python SimpleNamespace object containing the updated
            variable arrays in accordance with the MKS unit
            transforms.

        """

        # Collect the Python SimpleNamespace object containing the
        # native variable quantities and convert the native variable
        # quantities to MKS variable quantities.
        varobj = await func(*args, **kwargs)
        varobj_mks = varobj.to_base_units()

        return varobj_mks

    return wrapped_function
