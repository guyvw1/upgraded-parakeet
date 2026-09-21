


import httpx
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "https://api.neso.energy/api/3/action/datastore_search"
RESOURCE_ID = "7c0411cd-2714-4bb5-a408-adb065edf34d"

def fetch_records(limit: int = 100) -> list[dict]:
    """Fetch raw records from the NESO API."""
    response = httpx.get(API_URL, params={"resource_id": RESOURCE_ID, "limit": limit})
    return response.json()["result"]["records"]

def to_dataframe(records: list[dict]) -> pd.DataFrame:
    """Turn the records into a table."""
    return pd.DataFrame(records)

def show_summary(df: pd.DataFrame) -> None:
    """Print the size of the table and its first few rows."""
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nFirst 5 rows:")
    print(df.head())

    