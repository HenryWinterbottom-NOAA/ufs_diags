Oceanic Pressures
=================

.. currentmodule:: derived.ocean.pressures

.. autofunction:: seawater_from_depth

The following are the mandatory ``SimpleNamespace`` variables upon
entry. Note that all unit conversions are handled within the
respective function(s).

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - **Variable**
     - **Description**
   * - ``depth``
     - 3-dimensional array of oceanic depth values; ``z`` is positive
       and increases with depth.
   * - ``latitude``
     - 2-dimensional array of latitude coordinate values.
