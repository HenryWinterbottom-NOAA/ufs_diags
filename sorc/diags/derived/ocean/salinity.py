""" """

from types import SimpleNamespace

import os

import numpy
from gsw import SA_from_SP
from metpy.units import units

from utils.logger_interface import Logger
from diags.derived.derived import Derived, chunk_list

from diags.derived.ocean import pressures

# ----

# Define all available module properties.
__all__ = ["absolute_salinity_from_practical_salinity"]

# ----

logger = Logger(caller_name=__name__)

# ----


def absolute_salinity_from_practical_salinity(
        varobj: SimpleNamespace) -> numpy.array:
    """


    """

    msg = "Computing absolute salinity from practical salinity."
    logger.info(msg=msg)
    (lat, lon) = (varobj.latitude.values.magnitude.ravel(),
                  varobj.longitude.values.magnitude.ravel())
    (nz, ny, nx) = numpy.shape(varobj.salinity.values.magnitude)
    prac_sal = numpy.reshape(varobj.salinity.values.magnitude, (nz, ny*nx))
    swpres = numpy.reshape(varobj.seawater_pressure.values.magnitude,
                           (nz, ny*nx))

    @chunk_list(nx*ny)
    def compute_SA_from_SP():
        abs_sal = numpy.zeros((nz, (nx*ny)))
        for idx in range(len(chunks_list) - 1):
            abs_sal[:, chunks_list[idx]:chunks_list[idx + 1]] = SA_from_SP(
                SP=prac_sal[:, chunks_list[idx]:chunks_list[idx + 1]],
                p=swpres[:, chunks_list[idx]:chunks_list[idx + 1]],
                lat=lat[chunks_list[idx]:chunks_list[idx + 1]],
                lon=lon[chunks_list[idx]:chunks_list[idx + 1]]
            )

        return abs_sal

    abs_sal = compute_SA_from_SP()

    print(numpy.nanmin(abs_sal), numpy.nanmax(abs_sal))

    # chunk_list = Derived().chunk(ncoords=(nx*ny))
    # for idx in range(len(chunk_list)-1):
    #    abs_sal[:, chunk_list[idx]:chunk_list[idx+1]] = \
    #        SA_from_SP(SP=prac_sal[:, chunk_list[idx]:chunk_list[idx+1]],
    # p=swpres[:, chunk_list[idx]:chunk_list[idx+1]],
    #                  lat=lat[chunk_list[idx]:chunk_list[idx+1]],
    #                  lon=lon[chunk_list[idx]:chunk_list[idx+1]])


#    print((ny*nx)/os.cpu_count())
#    print(ny*nx)

#    print(os.cpu_count())

    quit()

    abs_sal = SA_from_SP(SP=prac_sal, p=swpres, lat=lat, lon=lon)
    # abs_sal = numpy.reshape(abs_sal, (nz, ny, nx))

    # abs_sal = [compute_SA_from_SP(prac_sal=prac_sal[:, idx],
    #                              swpres=swpres[:, idx],
    #                              lat=lat[idx],
    #                              lon=lon[idx]) for idx in range(nx*ny)]

    print(numpy.nanmin(abs_sal), numpy.nanmax(abs_sal))

    quit()

    # prac_sal = numpy.reshape(varobj.salinity.values.magnitude, (varobj.salinity.values.magnitude[0], numpy.shape
    # swpres=(varobj.seawater_pressure.values.to(
    #    units.dbar)).magnitude[:, ...].ravel()
    # (lat, lon)=(varobj.latitude.values.magnitude.ravel(),
    #              varobj.longitude.values.magnitude.ravel())

    # print(numpy.shape(prac_sal))
    # print(numpy.shape(lat))
    quit()

    # abs_sal = (units.Quantity(SA_from_SP(
    #    SP=prac_sal[:, 540:560, 720:790], p=swpres[:, 540:560, 720:790], lon=lon[540:560, 720:790], lat=lat[540:560, 720:790]), "g/kg"))

    # print(numpy.nanmin(abs_sal), numpy.nanmax(abs_sal))

    # print(abs_sal)

    # return abs_sal

    quit()
