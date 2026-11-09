import json
import pandas as pd
import os

# Load raw JSON data
raw_file_path = "data/raw_permits.json"
if os.path.exists(raw_file_path):
    with open(raw_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # Extract feature attributes
    features = data.get("features", [])
    records = [feat.get("attributes", {}) for feat in features]
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(records)
    
    # Cleaning & Tidy Steps:
    # 1. Rename columns to standard snake_case if necessary
    # 2. Filter out rows with missing essential metadata
    # 3. Restrict time window (2010-2025)
    
    # Example cleaning pipeline:
    if not df.empty:
        # Drop duplicates if any exist
        df = df.drop_duplicates()
        
        # Save a clean sample to repository (e.g., top 10 rows)
        sample_df = df.head(10)
        sample_output_path = "data/cleaned_permits_sample.csv"
        sample_df.to_csv(sample_output_path, index=False)
        print(f"Tidy sample saved successfully to {sample_output_path}!")
    else:
        print("DataFrame is empty. Check raw data structure.")
else:
    print("Raw data file not found. Run collection script first.")
