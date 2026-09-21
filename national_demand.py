import httpx
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "https://api.neso.energy/api/3/action/datastore_search"
RESOURCE_ID = "7c0411cd-2714-4bb5-a408-adb065edf34d"

# 1. Fetch the data
response = httpx.get(API_URL, params={"resource_id": RESOURCE_ID, "limit": 10000})
payload = response.json()
records = payload["result"]["records"]

# 2. Look at one row to see what fields exist
print("First record:", records[0])

# 3. Put it all in a DataFrame
df = pd.DataFrame(records)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 5 rows:")
print(df.head())

# 4. Convert GDATETIME to an actual datetime, sort chronologically
df["GDATETIME"] = pd.to_datetime(df["GDATETIME"])
df = df.sort_values("GDATETIME")

# 5. Plot national demand over time
plt.figure(figsize=(10, 5))
plt.plot(df["GDATETIME"], df["NATIONALDEMAND"])
plt.xlabel("Time (UTC)")
plt.ylabel("National Demand Forecast (MW)")
plt.title("GB National Demand Forecast")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("national_demand_forecast.png")
print("\nSaved chart to national_demand_forecast.png")