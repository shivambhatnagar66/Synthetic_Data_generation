import pandas as pd
import numpy as np                               
import matplotlib.pyplot as plt  

np.random.seed(42) 

# Step 1: Generate dummy data
print("Step 1: Creating our dummy signal")       
print("We'll create a signal that combines several different patterns")

# Parameters for our signal
duration = 5.0                                
sampling_rate = 1000                        
num_samples = int(duration * sampling_rate)     
time = np.linspace(0, duration, num_samples)      
print(f"Recording {duration} seconds at {sampling_rate} samples/second") 
print(f"Total samples: {num_samples}")

# Create a signal with multiple frequency components
print("\nOur signal will contain:")                      #displays the composition of our signal i.e. 5Hz, 20Hz and random noise
print("- A strong 5Hz wave (like a slow oscillation)")
print("- A weaker 20Hz wave (a faster oscillation)")
print("- Some random noise (like static)")

# Create the components using amplitude * sin(2*pi*frequency*time)
signal_5hz = 1.0 * np.sin(2 * np.pi * 5 * time)         
signal_20hz = 0.5 * np.sin(2 * np.pi * 20 * time)       
noise = 0.2 * np.random.randn(num_samples)              

# Combine everything into our final signal
signal = signal_5hz + signal_20hz + noise

#creating a dataframe
df = pd.DataFrame({
    "Time": time,
    "Signal": signal
})

df.to_csv("signal.csv", index = False)
print("signal.csv file generated.")