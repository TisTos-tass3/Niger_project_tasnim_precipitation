# Niger_project_tasnim_precipitation
README — Niger Precipitation Analysis

This project uses two separate scripts, which must be run in order:
1. climate_indices.sh — uses Bash and CDO to calculate annual precipitation (PR), SDII and R20mm from NetCDF files. It creates annual_indices.csv.
2. plot_graphs.py — uses Python to read the CSV and produce 12 graphs (3 indices × 4 experiments), comparing ACCESS-CM2, MPI-ESM1-2-HR and their ensemble mean.


Requirements
- Bash and CDO (e.g., Ubuntu or WSL)
- Python 3, pandas, matplotlib, and JupyterLab
- The required daily precipitation NetCDF (.nc) files
If needed, install CDO in Ubuntu with sudo apt install cdo, and the Python packages with pip install pandas matplotlib jupyterlab.


1. Adjust the paths
Before running either script, change the directories to match the folders on your own computer:
- In climate_indices.sh, edit INPUT (folder containing the .nc files) and OUTPUT (folder for results).
- In plot_graphs.py, edit DATA to point to the same results folder specified by OUTPUT above.



2. Run the Bash/CDO script
Open an Ubuntu/WSL terminal, navigate to the folder containing the Bash script, and run:

> bash climate_indices.sh

It creates annual_indices.csv in the chosen results folder. The script expects input filenames in the format:
pr_day_ACCESS-CM2_historical_r1i1p1f1_gn_1985_Africa.nc
The input files must cover 1985–2014 (historical) and 2019–2050 (each SSP) for both models.

3. Run the Python plotting script
Start JupyterLab:

> jupyter lab

Open the Python script in a notebook or copy its contents into a notebook cell, then execute it. Alternatively, run it directly with 
> python plot_graphs.py
from an environment where the required packages are installed.

It reads annual_indices.csv and saves the 12 PNG figures in the graphs subfolder of the results directory.
Expected output
results/
├── annual_indices.csv
└── graphs/
    ├── PR_historical.png
    ├── PR_ssp126.png
    ├── ...
    ├── SDII_*.png
    └── R20mm_*.png

Run order: Bash/CDO → CSV → Python/JupyterLab → 12 graphs.
