import os


def save_cleaned_data(df, out_dir="outputs"):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "cleaned_data.csv")
    try:
        df.to_csv(path, index=False)
        print(f"Cleaned data saved to {path}")
    except Exception as e:
        print(f"Could not save cleaned data: {e}")


def save_building_summary(summary_df, out_dir="outputs"):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "building_summary.csv")
    try:
        summary_df.to_csv(path, index=False)
        print(f"Building summary saved to {path}")
    except Exception as e:
        print(f"Could not save building summary: {e}")


def write_text_summary(df, building_summary, daily_totals, weekly_totals, out_dir="outputs"):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "summary.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write("Project summary\n")
            f.write(f"Rows in cleaned data: {len(df)}\n")
            f.write(f"Buildings: {len(building_summary)}\n")
            f.write(f"Daily periods: {len(daily_totals)}\n")
            f.write(f"Weekly periods: {len(weekly_totals)}\n")
        print(f"Text summary written to {path}")
    except Exception as e:
        print(f"Could not write text summary: {e}")
