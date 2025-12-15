# DSCI510_Final_Project
IMDb Top 250 Movie Analysis

Student: Jiachen Hu / Qi Shen

Project Name: Rating Patterns in IMDb Top 250 Films:
A Descriptive Analysis Across Time, Genre, and Runtime



Project Summary:

This project collects data from the IMDb Top 250 webpage, cleans the data, and creates several visualizations to explore trends such as:

~Ratings across different decade

~Ratings by genre

~Movie counts by decade

~Runtime–rating correlation



1. Create a virtual environment

Mac / Linux:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate



2. Install required libraries

Run the following:
```bash
pip install -r requirements.txt
```
This installs packages like requests, beautifulsoup4, pandas, and matplotlib.



3. How to Run the Scripts

Step 1 — Collect data
```bash
python src/get_data.py
```

This script scrapes IMDb Top 250 + each movie page, then saves raw data into:
```bash
data/raw/
```

Step 2 — Clean the data
```bash
python src/clean_data.py
```

Outputs cleaned data to:
```bash
data/processed/
```

Step 3 — Run analysis
```bash
python src/run_analysis.py
```

Creates decade/genre statistics (CSV files).

Step 4 — Generate visualizations
```bash
python src/visualize_results.py
```

Plots are saved to:
```bash
results/Visualizations.ipynb/
```



4. Project Structure
```
github_repo_structure/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── project_proposal.pdf
├── src/
│   ├── get_data.py
│   ├── clean_data.py
│   ├── run_analysis.py
│   └── visualize_results.py
└── results/
    ├── Visualizations.ipynb/
    └── final_report.pdf
```




5. Outputs

Clean movie dataset

Analysis summary CSVs

Four visualizations (JPG)

Final written report
