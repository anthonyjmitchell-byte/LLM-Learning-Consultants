# LLM Learning Consultants

AI applications, prompt engineering, fine-tuning, evaluation, and related tools. Focused on Python usage.

## Project Goals
- Document experiments, best practices, and consulting templates.
- Analyze data, use cases with notebooks.
- Share reusable code, prompts, and datasets
  
## Folder Structure
LLM-Learning-Consultants/
├── README.md
├── requirements.txt
├── .gitignore
├── notebooks/                 # Jupyter notebooks for experiments
│   ├── 01_prompt_engineering.ipynb
│   └── evaluation/            # Subfolder for metrics/benchmarks
├── src/                       # Reusable code
│   ├── init.py
│   ├── prompts.py             # Prompt templates
│   └── llm_utils.py           # API calls, evaluation helpers
├── data/                      # Small sample data/prompts only
│   ├── raw/                   # Original small files
│   └── processed/
├── docs/                      # Guides, notes, glossaries
│   ├── best-practices.md
│   └── figures/               # Screenshots, diagrams
└── .github/                   # Future workflows

## Tech Stack

### Languages
- Python 3.10+ (core language for scripts and notebooks)

### Frameworks & Libraries
- Jupyter / JupyterLab (interactive notebooks for experiments)
- Hugging Face Transformers (LLM models, tokenizers, pipelines)
- OpenAI SDK (or Groq, Anthropic, etc. for API access)
- Pandas & Openpyxl (data handling, if using Excel/CSV for prompts or evaluations)
- Matplotlib / Seaborn (visualizations of results)

### Tools & Environment
- Git & GitHub (version control and collaboration)
- Google Colab (optional cloud notebook execution)
- pip / venv (dependency management)
- .env files + python-dotenv (for API keys)

### Future
- Weights & Biases or MLflow (experiment tracking)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Transformers](https://img.shields.io/badge/Transformers-FF6F00?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/docs/transformers)
## Quick Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/anthonyjmitchelll-byte/LLM-Learning-Consultants.git
   cd LLM-Learning-Consultants
