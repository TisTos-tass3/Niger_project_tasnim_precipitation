import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("C:/path")


OUTPUT = DATA / "graphs"
OUTPUT.mkdir(parents=True, exist_ok=True)

# ==========================================
# 1. LOAD CSV DATA
# ==========================================

df = pd.read_csv(DATA / "annual_indices.csv")

print("Dataset preview:")
print(df.head())

# ==========================================
# 2. STUDY PARAMETERS
# ==========================================

models = ["ACCESS-CM2", "MPI-ESM1-2-HR"]

experiments = [
    "historical",
    "ssp126",
    "ssp245",
    "ssp585"
]

indices = {
    "PR": ("Annual Precipitation", "Precipitation (mm/year)"),
    "SDII": ("Simple Daily Intensity Index", "SDII (mm/wet day)"),
    "R20mm": ("Very Heavy Precipitation Days", "R20mm (days/year)")
}

colors = {
    "ACCESS-CM2": "blue",
    "MPI-ESM1-2-HR": "orange",
    "Ensemble Mean": "black"
}

# ==========================================
# 3. GENERATE THE 12 GRAPHS
# ==========================================

for index, (title, ylabel) in indices.items():

    for exp in experiments:

        # Select the experiment
        data = df[df["experiment"] == exp]

        # Organize values by year and model
        table = data.pivot(
            index="year",
            columns="model",
            values=index
        ).sort_index()

        table = table[models].copy()

        # Calculate ensemble mean
        table["Ensemble Mean"] = (
            table["ACCESS-CM2"] +
            table["MPI-ESM1-2-HR"]
        ) / 2

        # Define period
        if exp == "historical":
            period = "1985–2014"
        else:
            period = "2019–2050"

        # Create graph
        plt.figure(figsize=(12, 6.75))

        plt.plot(
            table.index,
            table["ACCESS-CM2"],
            label="ACCESS-CM2",
            color=colors["ACCESS-CM2"],
            linewidth=1.8
        )

        plt.plot(
            table.index,
            table["MPI-ESM1-2-HR"],
            label="MPI-ESM1-2-HR",
            color=colors["MPI-ESM1-2-HR"],
            linewidth=1.8
        )

        plt.plot(
            table.index,
            table["Ensemble Mean"],
            label="Ensemble Mean",
            color=colors["Ensemble Mean"],
            linewidth=2.5
        )

        # Graph formatting
        plt.title(
            f"Niger — {title}\n{exp.upper()} ({period})",
            fontsize=15,
            fontweight="bold"
        )

        plt.xlabel("Year", fontsize=12)
        plt.ylabel(ylabel, fontsize=12)

        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        # Save graph
        filename = OUTPUT / f"{index}_{exp}.png"

        plt.savefig(filename, dpi=300, bbox_inches="tight")

        # Display in JupyterLab
        plt.show()
        plt.close()

        print(f"Saved: {filename.name}")

# ==========================================
# 4. FINAL VERIFICATION
# ==========================================

graphs = list(OUTPUT.glob("*.png"))

print("\n===================================")
print("PROCESSING COMPLETED")
print("===================================")
print(f"Total graphs generated: {len(graphs)}")
print(f"Output directory: {OUTPUT}")

for graph in sorted(graphs):
    print(graph.name)
