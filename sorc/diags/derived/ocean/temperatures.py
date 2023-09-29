"""


"""

from metpy.units import units

import numpy
from gsw import CT_from_pt, t_from_CT
from types import SimpleNamespace
from diags.derived.derived import Derived


def insitu_from_potential(varobj: SimpleNamespace) -> numpy.array:
    """ """

    constants_obj = Derived().constants_obj

    salin = varobj.salinity.values.magnitude
    pottemp = varobj.pottemp.values.magnitude
    constemp = CT_from_pt(salin, pottemp)
    swpdbar = units.Quantity(varobj.seawater_pressure.values, "dbar")
    insitu = t_from_CT(salin, constemp, swpdbar)

    print(insitu)

    # p = varobj.pressure.values.magnitude - 10.0
    # insitu = t_from_CT(sa, ct, pres - 10.0))

    # ct = CT_from_pt(sa, pt)

    # print(ct)

    quit()

    return insitu
