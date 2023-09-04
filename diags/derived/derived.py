# =========================================================================
# File: diags/derived/derived.py
# Author: Henry R. Winterbottom
# Date: 09 March 2023
# Version: 0.0.1
# License: LGPL v2.1
# =========================================================================

"""
Module
------

    derived.py

Description
-----------

    This module contains the base-class object for all derived
    quantity classes.

Classes
-------

    Derived()

        This is the base-class object for all derived classes.

Requirements
------------

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 09 March 2023

History
-------

    2023-08-29: Henry Winterbottom -- Initial implementation.

"""

# ----

# pylint: disable=too-few-public-methods

# ----

__author__ = "Henry R. Winterbottom"
__maintainer__ = "Henry R. Winterbottom"
__email__ = "henry.winterbottom@noaa.gov"

# ----

from importlib import import_module
from typing import Callable, Generic

from exceptions import DerivedError
from tools import parser_interface
from utils.logger_interface import Logger

# ----


class Derived:
    """
    Description
    -----------

    This is the base-class object for all derived classes.

    """

    def __init__(self: Generic):
        """
        Description
        -----------

        Creates a new Derived object.

        """

        # Define the base-class attributes.
        self.logger = Logger(caller_name=f"{__name__}.{self.__class__.__name__}")

    def get_module(self: Generic, module: str, method: str) -> Callable:
        """
        Description
        -----------

        This method returns the function corresponding to the specified
        method (`method`) within the respective specified class
        (`module`).

        Parameters
        ----------

        module: str

            A Python string specifying the name of the module or
            package from which to collect the respective method.

        method: str

            The method or function within the module or package
            (`module`) to be returned.

        Returns
        -------

        compute_method: Callable

            A Python function within the specified module.

        """

        # Define the method/function within the specified module.
        try:
            compute_method = parser_interface.object_getattr(
                object_in=import_module(module), key=f"{method}", force=True
            )
        except Exception as errmsg:
            msg = (
                f"Collecting method {method} from module {module} failed with "
                f"error {errmsg}. Aborting!!!"
            )
            raise DerivedError(msg=msg) from errmsg

        return compute_method
