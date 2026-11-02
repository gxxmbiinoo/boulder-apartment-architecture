# Proposal: The Evolution of Boulder Apartment Architecture (2010–2025)

**Course:** Web Data Science (INFO 4617/5617)  
**Date:** October 25, 2026  
**Author:** Muhammed S. Jatta  

---

## 1. Research Question

### Question
How have the physical scale, structural dimensions, and architectural capacity characteristics (building height, total housing unit counts, square footage, and valuation) of newly permitted multi-family apartment buildings in Boulder, Colorado evolved between 2010 and 2025?

### Stakeholders
* **Local Municipalities & City Planners:** City of Boulder Housing and Human Services and Planning & Development Services evaluating the real-world impact of zoning updates and inclusionary housing mandates over time.
* **Architecture & Urban Design Firms:** Local developers and architects analyzing spatial and regulatory design constraints when proposing new residential infill projects.
* **Community Housing Advocates & Reporters:** Local journalists and housing policy researchers tracking whether construction matches municipal goals for urban density and housing supply.

### Expectations & Potential Surprises
* **Expectation:** I expect newly constructed multi-family apartment developments to trend steadily closer toward Boulder’s strict 55-foot height limit cap while increasing total housing unit density per building permit, particularly following key commercial and residential zoning updates post-2018.
* **Surprise:** It would be surprising if average building heights or unit densities declined over time despite surging regional land costs, or if square footage expanded while unit counts remained flat (indicating a shift toward low-density luxury units over high-density housing).

---

## 2. Data Source(s) and Method

### Exact Data Source
* **Primary Source:** City of Boulder Open Data Catalog & Enterprise MapServer GIS Endpoints.
* **Documentation:** [City of Boulder Open Data Portal](https://open-data.bouldercolorado.gov/)

### Method of Collection
* Data will be programmatically retrieved via REST API endpoints using Python (`requests` and `pandas`). 
* This relies on methods covered in course materials for REST APIs, JSON handling, and automated data extraction.

### Scope & Volume
* **Filtering Criteria:** Records where permit descriptions or types target multi-family or residential apartment structures.
* **Time Window:** Permits issued between January 1, 2010 and December 31, 2025.
* **Estimated Volume:** Approximately 600 to 1,500 individual multi-family construction permit records.

### Analysis & Visualizations
1. **Time-Series Analysis:** Line graphs tracking average and median building heights, valuation, and total square footage per permit from 2010 to 2025.
2. **Density Comparisons:** Bar charts comparing aggregate residential unit counts created per year before and after major local zoning policy shifts.
3. **Distributions:** Boxplots showing structural footprint variance across Boulder zoning districts.

---

## 3. Ethics and Feasibility

### Terms of Service & Robots.txt
* The City of Boulder Open Data Portal operates under an explicit open-access municipal policy (Public Domain / CC0 License) encouraging public research and data utilization.
* A custom HTTP `User-Agent` string will identify requests as academic research, and queries will include rate-limiting pauses between sequential calls.

### Personal Information Handling
* The dataset contains municipal public records, including property addresses, parcel numbers, and contractor names.
* **Privacy Plan:** Individual applicant names will be excluded or stripped during ingestion. All analytical results will be presented at an aggregate level without publishing private contact details.

### Retrieved Record Proof
```python
import requests

url = "[https://gis.bouldercolorado.gov/ags_svr3/rest/services/pw/BuildingFootprints/MapServer/0/query](https://gis.bouldercolorado.gov/ags_svr3/rest/services/pw/BuildingFootprints/MapServer/0/query)"
params = {"where": "1=1", "outFields": "*", "resultRecordCount": 1, "f": "json"}
headers = {"User-Agent": "CU-Boulder-Student-Research/1.0"}

response = requests.get(url, params=params, headers=headers)
print(f"Status Code: {response.status_code}")
