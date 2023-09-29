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

- metpy; https://unidata.github.io/MetPy/latest/index.html

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

import os
from importlib import import_module
from types import SimpleNamespace
from typing import Callable, Generic, List

from confs.yaml_interface import YAML
from diags.exceptions import DerivedError
from metpy.units import units
from tools import parser_interface
from utils.decorator_interface import privatemethod
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
        self.logger = Logger(
            caller_name=f"{__name__}.{self.__class__.__name__}")
        self.constants_obj = self.get_constants()

    def chunk(self: Generic, ncoords: int) -> List:
        """ """

        dchunk = int(ncoords/os.cpu_count())
        chunk_list = []
        chunk_size = 0
        for idx in range(os.cpu_count()):
            chunk_size = min(idx*dchunk, ncoords)
            chunk_list.append(chunk_size)
        chunk_list.append(ncoords)
        chunk_list = sorted(list(set(chunk_list)))

        return chunk_list

    @privatemethod
    def get_constants(self: Generic) -> SimpleNamespace:
        """
        Description
        -----------

        This method parses an external YAML-formatted file containing
        defined constant values and builds a SimpleNamespace object
        containing the attributes for each of the specified constant
        values.

        Returns
        -------

        constants_obj: SimpleNamespace

            A Python SimpleNamespace object containing the specified
            constant values attributes.

        Raises
        ------

        DerivedError:

            - raised if an exception is raised why defining the
              SimpleNamespace for the specified constant values
              attributes.

        """

        # Collect the specified constant values and compose the
        # base-class SimpleNamespace object.
        constants_obj = parser_interface.object_define()
        try:
            constants_yaml = os.path.join(
                parser_interface.enviro_get(envvar="DIAGS_ROOT"),
                "parm",
                "constants.yaml",
            )
            constants_dict = YAML().read_yaml(yaml_file=constants_yaml)
        except Exception as errmsg:
            msg = (
                "Defining the specified constant values failed with error ",
                f"{errmsg}. Aborting!!!",
            )
            raise DerivedError(msg=msg) from errmsg
        for constant in constants_dict:
            constant_value = constants_dict[constant]["value"]
            constant_units = constants_dict[constant]["units"]
            constants_obj = parser_interface.object_setattr(
                object_in=constants_obj,
                key=constant,
                value=units.Quantity(
                    constant_value,
                    parser_interface.object_getattr(
                        object_in=units, key=constant_units
                    ),
                ),
            )

        return constants_obj

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

# ----


def chunk_list(ncoords, *args, **kwargs):
    chunks_list = Derived().chunk(ncoords=ncoords)

    def function(func):
        def wrapper(*func_args, **func_kwargs):

            result = func(*func_args, *args, **kwargs)
            return result
        return wrapper
    return function
