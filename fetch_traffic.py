import requests
import pandas as pd

print("Fetching NYC traffic speed data...")

url = "https://data.cityofnewyork.us/resource/i4gi-tjb9.json"
params = {"$limit": 5000}

response = requests.get(url, params=params, timeout=15)
print("Status code:", response.status_code)

data = response.json()
df = pd.DataFrame(data)

df.to_csv("data/raw/traffic_raw.csv", index=False)
print(f"Saved {len(df)} rows to data/raw/traffic_raw.csv")
print(df.head())