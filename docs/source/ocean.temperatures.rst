Oceanic Temperatures
====================

.. currentmodule:: derived.ocean.temperatures

.. autofunction:: conservative_from_potential

The following are the mandatory SimpleNamespace variables upon
entry. Note that all unit conversions are handled within the
respective function(s).

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - **Variable**
     - **Description**
   * - ``lats``
     - Array of latitude coordinate values.
   * - ``lons``
     - Array of longitude coordinate values.
   * - ``ptemp``
     - Profile of potential temperature values.
   * - ``pres``
     - Profile of seawater pressure values.
   * - ``psaln``
     - Profile of practical salinity values.
		  
.. autofunction:: insitu_from_conservative

.. list-table::
   :widths: auto
   :header-rows: 1
   :align: left

   * - **Variable**
     - **Description**
   * - ``lats``
     - Array of latitude coordinate values.
   * - ``lons``
     - Array of longitude coordinate values.
   * - ``ptemp``
     - Profile of potential temperature values.
   * - ``pres``
     - Profile of seawater pressure values.
   * - ``psaln``
     - Profile of practical salinity values.
