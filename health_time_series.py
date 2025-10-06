import pandas as pd
import numpy as np

np.random.seed(42)

# Create daily dates
dates = pd.date_range(start="2023-01-01", periods=365, freq="D")

# Simulate health indicators with trend + seasonality + noise
glucose = 100 + 5*np.sin(np.linspace(0, 12*np.pi, 365)) + np.linspace(0, 10, 365) + np.random.normal(0, 5, 365)
systolic_bp = 120 + 8*np.sin(np.linspace(0, 6*np.pi, 365)) + np.random.normal(0, 6, 365)
cholesterol = 180 + 10*np.cos(np.linspace(0, 4*np.pi, 365)) + np.random.normal(0, 7, 365)

# Create DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Glucose": glucose.round(1),
    "Systolic_BP": systolic_bp.round(1),
    "Cholesterol": cholesterol.round(1)
})

# Save to CSV
df.to_csv("health_time_series.csv", index=False)

print("health_time_series.csv file generated with 365 days of data.")