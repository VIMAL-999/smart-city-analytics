import requests
import pandas as pd
import os
from datetime import datetime

url = "https://data.cityofnewyork.us/resource/i4gi-tjb9.json"
params = {"$limit": 5000}

response = requests.get(url, params=params, timeout=15)
data = response.json()
df = pd.DataFrame(data)
df["collected_at"] = datetime.utcnow().isoformat()

file_path = "data/raw/traffic_history.csv"

if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, mode="w", header=True, index=False)

print(f"[{datetime.utcnow().isoformat()}] Appended {len(df)} rows to {file_path}")