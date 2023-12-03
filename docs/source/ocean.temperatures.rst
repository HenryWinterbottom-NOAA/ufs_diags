Oceanic Temperatures
====================

.. currentmodule:: derived.ocean.temperatures

.. autofunction:: conservative_from_potential

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
   * - ``pottemp``
     - Profile of potential temperature values.
   * - ``seawater_pressure``
     - Profile of sea-water pressure values.
   * - ``salinity``
     - Profile of practical salinity values.
		  
.. autofunction:: insitu_from_conservative

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
   * - ``pottemp``
     - Profile of potential temperature values.
   * - ``seawater_pressure``
     - Profile of sea-water pressure values.
   * - ``salinity``
     - Profile of practical salinity values.
