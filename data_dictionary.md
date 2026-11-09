# Data Dictionary: Boulder Address Points & Multi-Family Units

This data dictionary defines each field contained in the cleaned dataset extracted from the City of Boulder’s Enterprise GIS Address Points endpoint.

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `OBJECTID` | Integer | Unique municipal system identifier for the address record. |
| `FULLADDR` | String | Complete formatted street address of the property or building in Boulder, CO. |
| `STATUS` | String | Operational status of the address point (e.g., Active, Retired, Under Construction). |
| `POINTTYPE` | String | Classification of the geographic point location (e.g., Building, Parcel, Unit). |
| `ADDRNUM` | Integer / String | Numerical street address number. |
| `UNITID` | String | Specific apartment, suite, or unit identifier (used to isolate multi-family apartment records). |
| `PREDIR` | String | Street name directional prefix (e.g., N, S, E, W). |
| `STREETNAME` | String | Primary name of the street (e.g., Broadway, 28th St, Arapahoe). |
| `STREETSUFFIX` | String | Street type suffix designation (e.g., St, Ave, Way, Pkwy). |
| `POSTDIR` | String | Street name directional suffix if applicable. |
| `CITY` | String | Municipality name, restricted to Boulder. |
| `STATE` | String | State code, restricted to Colorado (CO). |
| `ZIP5` | String | Primary 5-digit postal ZIP code. |
| `ZIP4` | String | Extended 4-digit postal ZIP code routing extension. |
