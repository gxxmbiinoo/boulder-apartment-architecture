# Evolution of Boulder Apartment Architecture (2010–2025)

**Author:** Muhammed S. Jatta  
**Course:** INFO 4617/5617: Web Data Science  
**Institution:** University of Colorado Boulder  

## Summary
How have the physical scale, structural dimensions, and architectural capacity characteristics (such as maximum building height, total housing unit density, square footage, and structural valuation) of newly permitted multi-family apartment buildings in Boulder, Colorado evolved between 2010 and 2025? This project leverages municipal building permit records and spatial APIs to empirically analyze how local zoning regulations, land costs, and policy updates have shaped urban multi-family residential development over a 15-year window.

---

## Data
* **Source:** City of Boulder Enterprise GIS MapServer Address Points Endpoint (`https://gis.bouldercolorado.gov/`).
* **Collection Timestamp:** Collected via automated script on November 8, 2026.
* **Record Count:** Sample batch of municipal address and multi-family unit location records.
* **What was left out of the repository and why:** 
  * The full raw GIS feature JSON containing extensive spatial coordinates and geometry arrays has been excluded from version control to adhere to repository size limits. 
  * A sanitized, tidy sample (`data/cleaned_permits_sample.csv`) containing core address attributes (`FULLADDR`, `STREETNAME`, `UNITID`) is provided to demonstrate the structured data pipeline.

## Methods
*Approach:* Programmatic REST API data extraction via Python (`requests`, `pandas`, `geopandas`), time-series aggregation, and statistical distribution comparison.

## Findings
*(Preliminary findings, data visualizations, and trend analysis charts will be posted here upon completion of the analysis notebook.)*

## How to Reproduce
1. Clone this repository: `git clone https://github.com/YOUR-USERNAME/boulder-apartment-architecture.git`
2. Open the analysis notebook (`analysis.ipynb`) in Jupyter Lab or VS Code.
3. Run the data ingestion scripts to pull live municipal records from Boulder’s open data endpoints.
