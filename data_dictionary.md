# Data Dictionary: Boulder Apartment Permits

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `permit_id` | Integer / String | Unique municipal identifier assigned to the construction or land-use permit. |
| `applied_date` | Date (YYYY-MM-DD) | The official calendar date when the permit application was submitted. |
| `permit_type` | String | Classification of the permit (e.g., Multi-Family New Construction, Residential Addition). |
| `description` | String | Detailed text description of the proposed building scope (e.g., "Construct 4-story apartment building"). |
| `valuation` | Float ($USD) | Estimated total monetary valuation of the construction work. |
| `building_height_ft` | Float | Maximum height of the structure in feet (analyzed against Boulder's 55ft limit). |
| `square_footage` | Integer | Gross total square footage of the permitted development. |
| `address` | String | Street address of the development parcel within Boulder, CO. |
| `zoning_district` | String | Municipal zoning designation code (e.g., RH-2, MU-3) governing density rules. |
