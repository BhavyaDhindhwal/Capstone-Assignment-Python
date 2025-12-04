import pandas as pd


def _ensure_datetime(df, date_col="date"):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    return df


def calculate_daily_totals(df):
    df = _ensure_datetime(df)
    daily = df.groupby(df["date"].dt.date)["energy_kwh"].sum().reset_index()
    daily.columns = ["date", "total_energy_kwh"]
    return daily


def calculate_weekly_aggregates(df):
    df = _ensure_datetime(df)
    weekly = (
        df.set_index("date").resample("W")["energy_kwh"].sum().reset_index()
    )
    weekly.columns = ["date", "weekly_energy_kwh"]
    return weekly


def building_wise_summary(df):
    summary = df.groupby("building")["energy_kwh"].agg(["sum", "mean", "count"]).reset_index()
    summary.columns = ["building", "total_kwh", "avg_kwh", "records"]
    return summary


def building_weekly_average(df):
    df = _ensure_datetime(df)
    bw = (
        df.groupby(["building", pd.Grouper(key="date", freq="W")])["energy_kwh"]
        .mean()
        .reset_index()
    )
    bw.columns = ["building", "week_end", "avg_kwh"]
    return bw
