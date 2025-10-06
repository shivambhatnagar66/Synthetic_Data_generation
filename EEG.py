import numpy as np
import pandas as pd

np.random.seed(42)

#Generating realistic EEG data with different brain wave patterns
# Parameters
duration = 30.0 
sampling_rate = 256 
num_samples = int(duration * sampling_rate) 
time = np.linspace(0, duration, num_samples)

print(f"Recording {duration} seconds at {sampling_rate} Hz (clinical standard)")            
print(f"Total samples: {num_samples}") 

# Brain wave frequency bands (in Hz)
delta_band = (0.5, 4) 
theta_band = (4, 8) 
alpha_band = (8, 13) 
beta_band = (13, 30) 
gamma_band = (30, 100)

print("\nBrain wave frequency bands we expect to find:")                             
print(f"- Delta waves ({delta_band[0]}-{delta_band[1]} Hz): Deep sleep, healing")    
print(f"- Theta waves ({theta_band[0]}-{theta_band[1]} Hz): Drowsiness, meditation") 
print(f"- Alpha waves ({alpha_band[0]}-{alpha_band[1]} Hz): Relaxed but awake")      
print(f"- Beta waves ({beta_band[0]}-{beta_band[1]} Hz): Active thinking, focus")    
print(f"- Gamma waves ({gamma_band[0]}-{gamma_band[1]} Hz): High-level processing")

# Create different brain wave components with realistic properties
delta_waves = 1.5 * np.sin(2 * np.pi * 2.0 * time)  
theta_waves = 1.2 * np.sin(2 * np.pi * 6.0 * time)  
alpha_waves = 2.0 * np.sin(2 * np.pi * 10.0 * time) 
beta_waves = 1.0 * np.sin(2 * np.pi * 18.0 * time)  
gamma_waves = 0.8 * np.sin(2 * np.pi * 40.0 * time)

# Add some variability to make it more realistic
for i in range(1, 5):
    delta_waves += 0.3 * np.sin(2 * np.pi * (2.0 + i*0.2) * time)   
    theta_waves += 0.25 * np.sin(2 * np.pi * (6.0 + i*0.3) * time)  
    alpha_waves += 0.4 * np.sin(2 * np.pi * (10.0 + i*0.4) * time)  
    beta_waves += 0.2 * np.sin(2 * np.pi * (18.0 + i*0.5) * time)   
    gamma_waves += 0.15 * np.sin(2 * np.pi * (40.0 + i*1.0) * time)  

# Eye blink artifact (common in EEG) - slow, high amplitude
eye_blinks = np.zeros(num_samples)                 
blink_times = [3, 8, 14, 21, 27]                   
for blink_time in blink_times:                     
    start_idx = int(blink_time * sampling_rate)    
    end_idx = start_idx + int(0.3 * sampling_rate) 
    if end_idx < num_samples:                      
        # Create a blink shape (sharp up, slow down)
        blink_duration = end_idx - start_idx       
        blink_shape = np.concatenate([ 
            np.linspace(0, 1, int(blink_duration * 0.2)), 
            np.linspace(1, 0, int(blink_duration * 0.8)) 
        ])
        # Make sure we don't exceed array bounds
        if start_idx + len(blink_shape) < num_samples:                           
            eye_blinks[start_idx:start_idx+len(blink_shape)] = 5.0 * blink_shape

# Muscle artifact (EMG) - high frequency noise
muscle_artifact = 0.4 * np.random.randn(num_samples) * np.sin(2 * np.pi * 60 * time)

# 50/60Hz power line interference (common artifact)
power_line_noise = 0.3 * np.sin(2 * np.pi * 50 * time)

# Random noise (sensor noise, environmental factors, etc.)
sensor_noise = 0.2 * np.random.randn(num_samples)

# Combine all components with different weights based on mental state
eeg_signal = (0.8 * delta_waves + 0.7 * theta_waves + 2.5 * alpha_waves +
              1.2 * beta_waves + 0.6 * gamma_waves +
              eye_blinks + muscle_artifact + power_line_noise + sensor_noise)

# Create a DataFrame
df = pd.DataFrame({
    "Time": time,
    "EEG": eeg_signal
})
df.to_csv("eeg_synthetic.csv", index = False)
print("eeg_synthetic.csv file generated.")