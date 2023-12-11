Oceanic Depths
==============

.. currentmodule:: derived.ocean.depths

.. autofunction:: depth_from_profile

The following are the mandatory ``SimpleNamespace`` variables upon
entry. Note that all unit conversions are handled within the
respective function(s).

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - **Variable**
     - **Description**
   * - ``depth_profile``
     - 1-dimentional array of oceanic depth profile values; ``z`` is
       positive and increases with depth.
   * - ``latitude``
     - 2-dimensional array of latitude coordinate values.
   * - ``longitude``
     - 2-dimensional array of longitude coordinate values.
