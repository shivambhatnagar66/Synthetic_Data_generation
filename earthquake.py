import numpy as np
import pandas as pd

np.random.seed(42)

#Generating realistic building vibration data
duration = 60.0 
sampling_rate = 100 
num_samples = int(duration * sampling_rate) 
time = np.linspace(0, duration, num_samples)

print(f"Recording {duration} seconds at {sampling_rate} Hz")
print(f"Total samples: {num_samples}")

# Real building characteristics (frequencies in Hz): These are the frequencies the building would naturally resonate at
natural_freq_1 = 0.8 #Fundamental frequency (1st mode)
natural_freq_2 = 2.5 #2nd mode
natural_freq_3 = 4.2 #3rd mode

# Earthquake components: These are the frequencies of the external force (the earthquake)
earthquake_freq_1 = 0.5 # Low frequency ground motion
earthquake_freq_2 = 3.0 # Medium frequency component
earthquake_freq_3 = 8.0 # High frequency component

print("\nBuilding natural frequencies:")
print(f"- 1st mode (swaying): {natural_freq_1} Hz")
print(f"- 2nd mode (bending): {natural_freq_2} Hz")
print(f"- 3rd mode (twisting): {natural_freq_3} Hz")

print("\nEarthquake frequencies (external forcing):")
print(f"- Low frequency: {earthquake_freq_1} Hz")
print(f"- Medium frequency: {earthquake_freq_2} Hz")
print(f"- High frequency: {earthquake_freq_3} Hz")

# Generate the signal components
building_response_1 = 2.0 * np.sin(2 * np.pi * natural_freq_1 * time) * np.exp(-0.01 * time)
building_response_2 = 1.2 * np.sin(2 * np.pi * natural_freq_2 * time) * np.exp(-0.02 * time)
building_response_3 = 0.8 * np.sin(2 * np.pi * natural_freq_3 * time) * np.exp(-0.03 * time)

# Earthquake forcing components
earthquake_component_1 = 1.5 * np.sin(2 * np.pi * earthquake_freq_1 * time)
earthquake_component_2 = 1.0 * np.sin(2 * np.pi * earthquake_freq_2 * time)
earthquake_component_3 = 0.7 * np.sin(2 * np.pi * earthquake_freq_3 * time)

# Random noise (sensor noise, environmental factors, etc.)
noise = 0.3 * np.random.randn(num_samples)

# Combine all components to create the final, complex vibration signal
vibration_signal = (building_response_1 + building_response_2 + building_response_3 +
                    earthquake_component_1 + earthquake_component_2 + earthquake_component_3 + noise)

# Create a DataFrame
df = pd.DataFrame({
    "Time": time,
    "Vibration": vibration_signal
})
df.to_csv("earthquake_vibration.csv", index = False)
print("earthquake_vibration.csv file generated.")