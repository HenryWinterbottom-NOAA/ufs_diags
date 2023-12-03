Oceanic Salinities
==================

.. currentmodule:: derived.ocean.salinity

.. autofunction:: absolute_from_practical

The following are the mandatory ``SimpleNamespace`` variables upon
entry. Note that all unit conversions are handled within the
respective function(s).
		 
.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - **Variable**
     - **Description**
   * - ``latitude``
     - Array of latitude coordinate values.
   * - ``longitude``
     - Array of longitude coordinate values.
   * - ``seawater_pressure``
     - Profile of seawater pressure values.
   * - ``salinity``
     - Profile of practical salinity values.
