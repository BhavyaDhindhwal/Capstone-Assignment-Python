class BuildingManager:
    def __init__(self):
        self.df = None

    def load_from_dataframe(self, df):
        self.df = df

    def print_reports(self):
        if self.df is None or self.df.empty:
            print("No building data available.")
            return

        buildings = self.df["building"].unique()
        print(f"Total buildings: {len(buildings)}")
        for b in buildings:
            subset = self.df[self.df["building"] == b]
            total = subset["energy_kwh"].sum()
            avg = subset["energy_kwh"].mean()
            print(f" Building {b}: total={total:.1f} kWh, avg={avg:.1f} kWh")
