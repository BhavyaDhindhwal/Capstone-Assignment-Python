import os


def create_dashboard(df, daily_totals, weekly_totals, weekly_building_avg):
    """Placeholder dashboard creator — writes a small text summary and returns.

    Creating full plots would require matplotlib; this keeps dependencies minimal.
    """
    out_dir = "outputs"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "dashboard_summary.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write("Dashboard summary\n")
        f.write(f"Rows in data: {len(df)}\n")
        f.write(f"Daily totals rows: {len(daily_totals)}\n")
        f.write(f"Weekly totals rows: {len(weekly_totals)}\n")
        f.write(f"Weekly building avg rows: {len(weekly_building_avg)}\n")

    print(f"Dashboard summary written to {path}")
