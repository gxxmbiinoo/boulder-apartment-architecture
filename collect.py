import requests
import json
import time
import os

# Creating data directory
os.makedirs("data", exist_ok=True)

# Endpoint for Boulder building / construction records
url = "https://gis.bouldercolorado.gov/ags_svr1/rest/services/plan/AddressPoints/MapServer/0/query"

params = {
    "where": "1=1",
    "outFields": "*",
    "resultRecordCount": 100,  # Batch size for polite polling
    "f": "json"
}

# Polite headers identifying the request as academic research
headers = {
    "User-Agent": "CU-Boulder-Student-Research-MuhammedJatta/1.0 (Educational Project)"
}

print("Beginning polite data collection...")
response = requests.get(url, params=params, headers=headers)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    raw_data = response.json()
    
    # Save raw data locally
    raw_file_path = "data/raw_permits.json"
    with open(raw_file_path, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=4)
        
    print(f"Success! Saved raw response to {raw_file_path}")
    
    # Polite pause
    time.sleep(1.5)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
