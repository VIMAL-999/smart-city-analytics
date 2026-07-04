import requests
import pandas as pd
from dotenv import load_dotenv
import os
import time

load_dotenv()
API_KEY = os.getenv("OPENAQ_API_KEY")
headers = {"X-API-Key": API_KEY}

# Step 1: Get NYC stations
locations_url = "https://api.openaq.org/v3/locations"
params = {"coordinates": "40.7128,-74.0060", "radius": 25000, "limit": 20}
response = requests.get(locations_url, headers=headers, params=params, timeout=15)
locations_data = response.json()["results"]

print(f"Found {len(locations_data)} stations. Pulling measurements...")

all_measurements = []

for loc in locations_data:
    location_id = loc["id"]
    location_name = loc["name"]

    # Each location has one or more "sensors" (PM2.5, NO2, etc.)
    for sensor in loc.get("sensors", []):
        sensor_id = sensor["id"]
        parameter = sensor["parameter"]["name"]

        measurements_url = f"https://api.openaq.org/v3/sensors/{sensor_id}/measurements"
        m_params = {"limit": 100, "sort": "desc"}

        try:
            m_response = requests.get(measurements_url, headers=headers, params=m_params, timeout=15)
            m_data = m_response.json().get("results", [])

            for m in m_data:
                all_measurements.append({
                    "location_id": location_id,
                    "location_name": location_name,
                    "parameter": parameter,
                    "value": m["value"],
                    "unit": m["parameter"]["units"] if "parameter" in m else None,
                    "date": m["period"]["datetimeFrom"]["utc"]
                })
        except Exception as e:
            print(f"Skipped sensor {sensor_id} ({parameter}) due to error: {e}")

        time.sleep(0.5)  # be polite to the API, avoid rate limits

df = pd.DataFrame(all_measurements)
df.to_csv("data/raw/air_quality_raw.csv", index=False)
print(f"Saved {len(df)} rows to data/raw/air_quality_raw.csv")