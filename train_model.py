import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
import joblib

df = pd.read_csv("data/processed/master_dataset.csv")

features = ["hour", "day_of_week", "avg_energy_demand"]
target = "pm25"

X = df[features]
y = df[target]

# ---------- Try two models, compare them honestly ----------
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

for name, model in models.items():
    # 5-fold cross-validation: trains/tests 5 times on different slices, more reliable on small data
    scores = cross_val_score(model, X, y, cv=5, scoring="neg_mean_absolute_error")
    mae = -scores.mean()
    print(f"{name}: Average MAE across 5 folds = {mae:.3f}")

# ---------- Train the better one on full data and save it ----------
final_model = RandomForestRegressor(n_estimators=100, random_state=42)
final_model.fit(X, y)

joblib.dump(final_model, "pm25_model.pkl")
print("\nSaved trained model to pm25_model.pkl")

# ---------- Show feature importance (which factor matters most) ----------
importances = pd.Series(final_model.feature_importances_, index=features)
print("\nFeature importance:")
print(importances.sort_values(ascending=False))