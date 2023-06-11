# =========================================================================

# Module: derived/atmos/atmos.py

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
Module
------

    atmos.py

Description
-----------

    This module contains the base-class for all derived atmosphere
    variables and/or quantities.

Classes
-------

    Atmos()

        This is the base-class object for all derived atmosphere
        variables; it is a sub-class of Derived.

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

from derived import Derived


from types import SimpleNamespace

import numpy

from exceptions import DerivedError

# ----


class Atmos(Derived):
    """
    Description
    -----------

    This is the base-class object for all derived atmosphere
    variables; it is a sub-class of Derived.

    """

    def __init__(self: Derived):
        """
        Description
        -----------

        Creates a new Atmos object.

        """

        # Define the base-class attributes.
        super().__init__()

    def compute_height(self: Derived, varobj: SimpleNamespace,
                       method: str) -> numpy.array:
        """
        Description
        -----------

        This method computes a height diagnostic type using the
        specified method.

        Parameters
        ----------

        varobj: SimpleNamespace

            A Python SimpleNamespace object containing, at minimum,
            the variables required for the respective height
            diagnostic computation.

        method: str

            A Python string specifying the method beneath
            `derived.atmos.heights`; currently supported methods are
            the following.

            - height_from_pressure

        Returns
        -------

        height: numpy.array

            A Python numpy.array variable containing the computed
            height values.

        """

        # Compute the respective height type from the specified
        # method.
        compute_module = "derived.atmos.heights"
        compute_method = self.get_module(module=compute_module, method=method)
        height = compute_method(varobj=varobj)

        return height

    def compute_moisture(self: Derived, varobj: SimpleNamespace,
                         method: str) -> numpy.array:
        """
        Description
        -----------

        This method computes a height diagnostic type using the
        specified method.

        Parameters
        ----------

        varobj: SimpleNamespace

            A Python SimpleNamespace object containing, at minimum,
            the variables required for the respective moisture type
            computation.

        method: str

            A Python string specifying the method beneath
            `derived.atmos.moisture`; currently supported methods are
            the following.

            - spfh_to_mxrt

        Returns
        -------

        moisture: numpy.array

            A Python numpy.array variable containing the computed
            moisture-type values.

        """

        # Compute the respective moisture type from the specified
        # method.
        compute_module = "derived.atmos.moisture"
        compute_method = self.get_module(module=compute_module, method=method)
        moisture = compute_method(varobj=varobj)

        return moisture

    def compute_pressure(self: Derived, varobj: SimpleNamespace,
                         method: str) -> numpy.array:
        """
        Description
        -----------

        This method computes a pressure type using the specified
        method.

        Parameters
        ----------

        varobj: SimpleNamespace

            A Python SimpleNamespace object containing, at minimum,
            the variables required for the respective pressure
            computation.

        method: str

            A Python string specifying the method beneath
            `derived.atmos.pressures`; currently supported methods are
            the following.

            - pressure_from_thickness

            - pressure_to_sealevel

        Returns
        -------

        pressure: numpy.array

            A Python numpy.array variable containing the computed
            pressure values.

        """

        # Compute the respective pressure type from the specified
        # method.
        compute_module = "derived.atmos.pressures"
        compute_method = self.get_module(module=compute_module, method=method)
        pressure = compute_method(varobj=varobj)

        return pressure

    def compute_wind(self: Derived, varobj: SimpleNamespace,
                     method: str) -> numpy.array:
        """
        Description
        -----------

        This method computes a wind-diagnostic type using the
        specified method.

        Parameters
        ----------

        varobj: SimpleNamespace

            A Python SimpleNamespace object containing, at minimum,
            the variables required for the respective wind-diagnostic
            computation.

        method: str

            A Python string specifying the method beneath
            `derived.atmos.winds`; currently supported methods are the
            following.

            - global_divg

            - global_vort

            - global_wind_part

            - wndmag

        Returns
        -------

        wind: numpy.array

            A Python array-type variable containing the computed
            wind-type values.

        """

        # Compute the respective wind-diagnostic type from the
        # specified method.
        compute_module = "derived.atmos.winds"
        compute_method = self.get_module(module=compute_module, method=method)
        wind = compute_method(varobj=varobj)

        return wind