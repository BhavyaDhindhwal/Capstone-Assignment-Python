import os
import glob
import pandas as pd


def load_and_merge_csv(data_dir="data"):
    """Load CSV files from `data_dir`. If none found, return a small sample DataFrame."""
    if os.path.isdir(data_dir):
        pattern = os.path.join(data_dir, "*.csv")
        files = glob.glob(pattern)
        if files:
            dfs = [pd.read_csv(f) for f in files]
            return pd.concat(dfs, ignore_index=True)

    # No data found — return a small synthetic dataset so pipeline can run
    dates = pd.date_range(end=pd.Timestamp.today(), periods=14, freq="D")
    data = []
    buildings = ["A", "B", "C"]
    for i, d in enumerate(dates):
        for b in buildings:
            data.append({
                "building": b,
                "date": d.strftime("%Y-%m-%d"),
                "energy_kwh": 10 + (i % 5) + (ord(b) % 7),
            })

    df = pd.DataFrame(data)
    return df
