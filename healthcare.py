# ================================
# 1. Generate Synthetic Healthcare Data
# ================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# Example: Healthcare data for 200 patients
n = 200
age = np.random.randint(30, 80, n)
blood_pressure = np.random.normal(120, 15, n)
cholesterol = np.random.normal(200, 25, n)
treatment_group = np.random.choice(['A', 'B'], size=n)
recovery_time = np.random.normal(10, 3, n) - (treatment_group == 'B') * 1.5  # Treatment B recovers faster
survival_time = np.random.exponential(365, n)  # in days
event_observed = np.random.binomial(1, 0.7, n) # 1 = event occurred, 0 = censored

df = pd.DataFrame({
    'Age': age,
    'BloodPressure': blood_pressure,
    'Cholesterol': cholesterol,
    'Treatment': treatment_group,
    'RecoveryTime': recovery_time,
    'SurvivalTime': survival_time,
    'EventObserved': event_observed
})
#save the dataset in your system
df.to_csv('healthcare.csv', index = False)
print("healthcare.csv file generated.")