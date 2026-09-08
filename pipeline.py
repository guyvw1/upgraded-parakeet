"""
The same demo as api_demo.py, split into functions.

Once a script grows past a few steps, this is the usual next move: each
function does one job, and main() reads like a summary of the whole thing.

Run it with:  uv run pipeline.py
"""

import httpx
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "https://api.neso.energy/api/3/action/datastore_search"
RESOURCE_ID = "8ba48f26-d73e-4094-a90d-ba075eb739c1"


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


def plot_status_counts(df: pd.DataFrame, output_path: str = "order_status.png") -> None:
    """Plot how many orders were executed vs rejected."""
    status_counts = df["status"].value_counts()
    print("\nOrder status counts:")
    print(status_counts)

    status_counts.plot(kind="bar", title="Auction order status")
    plt.xlabel("Status")
    plt.ylabel("Number of orders")
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"\nSaved chart to {output_path}")


def main() -> None:
    records = fetch_records()
    df = to_dataframe(records)
    show_summary(df)
    plot_status_counts(df)


# Only run main() when this file is run directly, not when it's imported.
if __name__ == "__main__":
    main()
