import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/iot_sensor_data.csv")

# Plot 1: Temperature vs Failure
plt.figure()
plt.scatter(df['temperature'], df['failure'])
plt.xlabel("Temperature")
plt.ylabel("Failure")
plt.title("Temperature vs Failure")
plt.savefig("outputs/temp_vs_failure.png")
print("📊 Saved: temp_vs_failure.png")

# Plot 2: Vibration vs Failure
plt.figure()
plt.scatter(df['vibration'], df['failure'])
plt.xlabel("Vibration")
plt.ylabel("Failure")
plt.title("Vibration vs Failure")
plt.savefig("outputs/vibration_vs_failure.png")
print("📊 Saved: vibration_vs_failure.png")

# Plot 3: Current vs Failure
plt.figure()
plt.scatter(df['current'], df['failure'])
plt.xlabel("Current")
plt.ylabel("Failure")
plt.title("Current vs Failure")
plt.savefig("outputs/current_vs_failure.png")
print("📊 Saved: current_vs_failure.png")

plt.show()