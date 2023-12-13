"""
Module
------

    fft.py

Description
-----------

    This module contains functional wrappers for the available numpy
    fast-Fourier transform applications.

Functions
---------

    forward_fft2d(varin)

        This function computes the forward fast Fourier transform
        (FFT) of a 2-dimensional real-value input array `varin`.

    inverse_fft2d(varin)

        This function computes the forward fast Fourier transform
        (FFT) of a 2-dimensional complex-value input array `varin`.

Requirements
------------

- ufs_pyutils; https://github.com/HenryWinterbottom-NOAA/ufs_pyutils

Author(s)
---------

    Henry R. Winterbottom; 16 March 2023

History
-------

    2023-03-16: Henry Winterbottom -- Initial implementation.

"""

# ----

import numpy
from exceptions import TransformsError
from utils.logger_interface import Logger

# ----

# Define all available module properties.
__all__ = ["forward_fft2d", "inverse_fft2d"]

# ----

logger = Logger(caller_name=__name__)

# ----


def forward_fft2d(varin: numpy.array) -> complex:
    """
    Description
    -----------

    This function computes the forward fast Fourier transform (FFT) of
    a 2-dimensional real-value input array `varin`.

    Parameters
    ----------

    varin: ``numpy.array``

        A Python numpy.array variable containing the 2-dimensional
        real-values input array.

    Returns
    -------

    varout: ``complex``

        A Python numpy.complex variable containing the 2-dimensional
        complex-values computed from the forward FFT.

    Raises
    ------

    TransformsError:

        - raised if the input array is not of 2-dimensions.

    """

    # Compute the forward fast Fourier transform in the input variable
    # array.
    if len(varin.shape) != 2:
        msg = (
            "The input array is not 2-dimensions; received an array of "
            f"{len(varin.shape)} dimensions. Aborting!!!"
        )
        raise TransformsError(msg=msg)
    msg = (
        "Computing the forward Fourier transform of input array dimension "
        f"({varin.shape[0]}, {varin.shape[1]})."
    )
    logger.info(msg=msg)
    varout = numpy.fft.fft2(varin)

    return varout


# ----


def inverse_fft2d(varin: complex) -> complex:
    """
    Description
    -----------

    This function computes the inverse fast Fourier transform (FFT) of
    a 2-dimensional complex-value input array `varin`.

    Parameters
    ----------

    varin: ``complex``

        A Python numpy.complex variable containing the 2-dimensional
        complex-values computed from the FFT.

    Returns
    -------

    varout: ``complex``

        A Python numpy.complex variable containing the 2-dimensional
        complex-values computed from the inverse FFT.

    Raises
    ------

    TransformsError:

        - raised if the input array is not of 2-dimensions.

    """

    # Compute the inverse fast Fourier transform in the input variable
    # array.
    if len(varin.shape) != 2:
        msg = (
            "The input array is not 2-dimensions; received an array of "
            f"{len(varin.shape)} dimensions. Aborting!!!"
        )
        raise TransformsError(msg=msg)
    msg = (
        "Computing the inverse Fourier transform of input array dimension "
        f"({varin.shape[0]}, {varin.shape[1]})."
    )
    logger.info(msg=msg)
    varout = numpy.fft.ifft2(varin)

    return varout
