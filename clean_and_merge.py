import pandas as pd

# ---------- AIR QUALITY ----------
air = pd.read_csv("data/raw/air_quality_raw.csv")
air = air.dropna(subset=["value"])

air["date"] = pd.to_datetime(air["date"])
air["hour"] = air["date"].dt.hour
air["day_of_week"] = air["date"].dt.dayofweek  # 0 = Monday

air_pivot = air.pivot_table(
    index=["hour", "day_of_week"],
    columns="parameter",
    values="value",
    aggfunc="mean"
).reset_index()

air_pivot.columns.name = None
print("Air quality pattern table:")
print(air_pivot.head())

# ---------- ENERGY ----------
energy = pd.read_csv("data/raw/energy_raw.csv")
energy["period"] = pd.to_datetime(energy["period"], format="%Y-%m-%dT%H")
energy["hour"] = energy["period"].dt.hour
energy["day_of_week"] = energy["period"].dt.dayofweek

energy_pattern = energy.groupby(["hour", "day_of_week"])["value"].mean().reset_index()
energy_pattern = energy_pattern.rename(columns={"value": "avg_energy_demand"})
print("\nEnergy pattern table:")
print(energy_pattern.head())

# ---------- MERGE ----------
master = pd.merge(air_pivot, energy_pattern, on=["hour", "day_of_week"], how="inner")

# Check how much missing data each pollutant column has
print("\nMissing values per column (out of", len(master), "rows):")
print(master.isnull().sum())

# Keep only the reliable columns: hour, day_of_week, pm25, o3, no2, energy demand
# (co, no, nox, pm10, so2 had too many gaps to be trustworthy)
keep_cols = ["hour", "day_of_week", "pm25", "o3", "no2", "avg_energy_demand"]
master_clean = master[keep_cols].copy()

# Drop any remaining rows with missing values in our chosen columns
master_clean = master_clean.dropna()

master_clean.to_csv("data/processed/master_dataset.csv", index=False)
print(f"\nSaved cleaned master dataset with {len(master_clean)} rows to data/processed/master_dataset.csv")
print(master_clean.head())