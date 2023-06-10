# =========================================================================

# Module: derived/__init__.py

# Author: Henry R. Winterbottom

# Email: henry.winterbottom@noaa.gov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the respective public license published by the
# Free Software Foundation and included with the repository within
# which this application is contained.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# =========================================================================

"""


"""

# ----

__author__ = "Henry R. Winterbottom"
__maintainer__ = "Henry R. Winterbottom"
__email__ = "henry.winterbottom@noaa.gov"

# ----

from dataclasses import dataclass

from importlib import import_module
from typing import Callable

from utils.logger_interface import Logger

# ----


@dataclass
class Derived:
    """
    Description
    -----------

    This is the base-class object for all derived classes.

    """

    def __init__(self: dataclass):
        """
        Description
        -----------

        Creates a new Derived object.

        """

        # Define the base-class attributes.
        self.logger = Logger(
            caller_name=f"{__name__}.{self.__class__.__name__}")

    def get_module(module: str, method: str) -> Callable:
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
