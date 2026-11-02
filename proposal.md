# Portfolio Project Proposal: The Evolution of Boulder, Colorado’s Apartment Architecture (2010 – 2025)

**Author:** Muhammed Jatta  
**Course:** INFO 4617: Web Data Science  

---

## 1. Research Question

### Question
Within the last 15 years, how have the physical scale, characteristics, and environment of newly permitted apartment complexes in the city of Boulder shifted and evolved?

### Stakeholders
Stakeholders include municipal urban planners, local architecture firms, housing advocacy coalitions or organizations, and city council members who specifically evaluate the real-world impact of the city’s height limit and high-density zoning reforms. Local journalists and housing policy researchers are also important stakeholders in this process.

### Expectations and Potential Surprises
I expect that there will be a lot of newly constructed multi-family developments that constantly hover around that 55-foot mark. I expect this to be seen especially clearly within the past 10 years. I’d be surprised if the amount of apartment buildings has gone down over the last few years. If it was a situation where people in the Boulder region are only building in certain areas I would understand, but I expect to see an upward trend.

---

## 2. Data Source(s) and Method

### Data Source
* **Primary Source:** City of Boulder Open Data Catalog – Building Permits Dataset
* **URL Endpoint:** `https://open-data.bouldercolorado.gov/api/explore/v2.1/catalog/datasets/building-permits/records`
* **Documentation:** [City of Boulder Open Data Portal](https://open-data.bouldercolorado.gov/)

### Method of Collection
The data will be retrieved with the OpenDataSoft REST API from Chapter 2 and 3 and this will be done with Python.

### Scope and Volume
I’ll be sure to filter variables related to `permit_type` or `description` since those will actually tell us what type of unit it is. I’ll also need to narrow the time down from January 1, 2010 to December 31, 2025 to cover the full 15-year study period. The volume will be approximately 500 to 2,000 units within the last 15 years.

### Analysis & Visualizations
I’ll be using a form of time-series analysis like a line graph to be able to track the average and median building heights, valuation, and total square footage per permit within the 15-year interval. Bar charts can help us compare the count of units or specify the scope of what we want to look for. Boxplots are essential for showing the variance across the different zoning districts all over the city.

---

## 3. Ethics and Feasibility

### Terms of Service / Robots.txt
The city of Boulder Open Data Portal operates under an open-access municipal policy, this encourages public research and data utilization. In order to make sure I have the best practices and won’t hit API rate limits, I'll use `time.sleep()` to pause in between API requests and I'll also be using a custom HTTP User-Agent string that will identify the request as research.

### Personal Information Handling
The dataset contains public records, property addresses, parcel numbers, and applicant company handles. In order to keep sensitive information private, I will be excluding homeowner and applicant information. Any analytical results will be presented at an aggregate level.

### Retrieved Record Proof
```python
import requests

# Live City of Boulder GIS MapServer query endpoint for Building / Permit data
url = "[https://gis.bouldercolorado.gov/ags_svr1/rest/services/plan/AddressPoints/MapServer/0/query](https://gis.bouldercolorado.gov/ags_svr1/rest/services/plan/AddressPoints/MapServer/0/query)"
params = {
    "where": "1=1",
    "outFields": "*",
    "resultRecordCount": 1,
    "f": "json"
}
headers = {"User-Agent": "CU-Boulder-Student-Research/1.0"}

response = requests.get(url, params=params, headers=headers)
print(f"Status Code: {response.status_code}")
data = response.json()
print("Retrieved Record Sample:")
print(data['features'][0]['attributes'])
