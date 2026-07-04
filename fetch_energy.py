import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("EIA_API_KEY")

print("Fetching NY energy demand data...")

url = "https://api.eia.gov/v2/electricity/rto/region-data/data/"
params = {
    "api_key": API_KEY,
    "frequency": "hourly",
    "data[0]": "value",
    "facets[respondent][]": "NY",
    "facets[type][]": "D",          # D = Demand
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "offset": 0,
    "length": 5000
}

response = requests.get(url, params=params, timeout=15)
print("Status code:", response.status_code)

data = response.json()

if "response" in data and "data" in data["response"]:
    df = pd.DataFrame(data["response"]["data"])
    df.to_csv("data/raw/energy_raw.csv", index=False)
    print(f"Saved {len(df)} rows to data/raw/energy_raw.csv")
    print(df.head())
else:
    print("Something went wrong. Full response below:")
    print(data)