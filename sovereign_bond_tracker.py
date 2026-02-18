import pandas as pd
import matplotlib.pyplot as plt

# Load data 
data = pd.read_csv("sovereign_yields.csv")

# Convert date column
data["Date"] = pd.to_datetime(data["Date"])

# Plot yields
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Yield"], label="10Y Sovereign Yield", color="navy")

plt.title("Sovereign Bond Yield Over Time")
plt.xlabel("Date")
plt.ylabel("Yield (%)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
