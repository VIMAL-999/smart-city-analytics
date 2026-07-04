import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the RAW energy data (real time series, not the averaged pattern table)
energy = pd.read_csv("data/raw/energy_raw.csv")
energy["period"] = pd.to_datetime(energy["period"], format="%Y-%m-%dT%H")

# Prophet requires columns named exactly "ds" (date) and "y" (value)
df = energy[["period", "value"]].rename(columns={"period": "ds", "value": "y"})

# Sort chronologically (our raw pull was newest-first, Prophet wants oldest-first)
df = df.sort_values("ds").reset_index(drop=True)

print(f"Training on {len(df)} hourly readings")
print(f"Date range: {df['ds'].min()} to {df['ds'].max()}")

# ---------- Train Prophet ----------
model = Prophet(daily_seasonality=True, weekly_seasonality=True)
model.fit(df)

# ---------- Forecast the next 48 hours ----------
future = model.make_future_dataframe(periods=48, freq="h")
forecast = model.predict(future)

# Show just the forecasted (future) part
future_only = forecast[forecast["ds"] > df["ds"].max()]
print("\nNext 48 hours forecast (demand in megawatthours):")
print(future_only[["ds", "yhat", "yhat_lower", "yhat_upper"]].head(10))

# Save the full forecast
forecast.to_csv("data/processed/energy_forecast.csv", index=False)
print("\nSaved forecast to data/processed/energy_forecast.csv")

# Save a plot so you can see it visually
fig = model.plot(forecast)
fig.savefig("energy_forecast_plot.png")
print("Saved chart to energy_forecast_plot.png")