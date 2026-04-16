## Folder Structure
LLM-Learning-Consultants/
├── README.md
├── requirements.txt
├── .gitignore
├── .nojekyll
├── index.html
├── results.html
├── survey.html
├── data/                  # Survey data (raw + processed)
├── src/                   # Python analysis scripts
├── docs/
│   └── figures/           # All charts used on the website (standardized path)
├── notebooks/             # Jupyter notebooks for experiments
├── Figures/               # Optional older folder for radar/bar charts
└── css/                   # Stylesheets (if any)

All graphs on the **results.html** page now use the standardized `docs/figures/` path for consistency.

## How to Update Results

To keep the survey analysis and visualizations current when new responses are collected:

1. Add new survey data to `data/survey_responses.csv` (or the Excel file `Impact of Large Language Models .xlsx`).
2. Run the analysis script:
   ```bash
   python src/analyze_survey.py
