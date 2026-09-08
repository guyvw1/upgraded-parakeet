"""
Read data from a public API, put it in a table, draw a chart.

Run it with:  uv run api_demo.py
"""

import httpx  # fetches things over the internet
import pandas as pd  # tables of data
import matplotlib.pyplot as plt  # charts

# NESO publishes free UK energy market data. Every dataset on their portal
# has an "API" button that shows its resource id.
API_URL = "https://api.neso.energy/api/3/action/datastore_search"
RESOURCE_ID = "8ba48f26-d73e-4094-a90d-ba075eb739c1"

# 1. Fetch the data. `params` becomes ?resource_id=...&limit=100 on the URL.
response = httpx.get(API_URL, params={"resource_id": RESOURCE_ID, "limit": 100})
records = response.json()["result"]["records"]

# 2. Look at one row to see what fields exist
print("First record:", records[0])

# 3. Put it all in a DataFrame - a table, like a spreadsheet
df = pd.DataFrame(records)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 5 rows:")
print(df.head())

# 4. Count executed vs rejected orders, and plot it
status_counts = df["status"].value_counts()
print("\nOrder status counts:")
print(status_counts)

status_counts.plot(kind="bar", title="Auction order status")
plt.xlabel("Status")
plt.ylabel("Number of orders")
plt.tight_layout()
plt.savefig("order_status.png")
print("\nSaved chart to order_status.png")

