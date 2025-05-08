# Financial Behavior Risk Profiler

This project uses machine learning to analyze and predict financial behavior risk profiles based on real and synthetic datasets. Designed for use in banking and fintech applications, this pipeline can be extended for credit scoring, loan default prediction, and risk-aware customer profiling.

## Project Structure

| File / Folder                        | Description |
|-------------------------------------|-------------|
| `analyze_risk.py`                   | Core script for training ML models and analyzing financial risk. |
| `check_columns.py`                  | Validates the structure and completeness of input datasets. |
| `generate_data.py`                  | Generates synthetic financial data for model training. |
| `load_data.py`                      | Loads and prepares data from CSV into SQLite database. |
| `financial_data.csv`               | Raw dataset containing real-world financial data. |
| `generated_data.csv`               | Synthetic data generated to augment the dataset. |
| `generated_data_with_features.csv` | Dataset with additional engineered features used in ML. |
| `financial_data.db`                | SQLite database version of the financial dataset. |
| `data/`                             | Placeholder for input data files or external datasets. |
| `db/`                               | Folder storing database files used in the project. |
| `requirements.txt`                 | List of Python dependencies required to run the project. |
| `README.md`                         | Project overview and documentation (this file). |



## Features

- Clean data ingestion pipeline from CSV to SQLite
- Synthetic data generation with customizable logic
- Automated column validation
- Feature engineering support
- Machine Learning risk analysis with model training and evaluation


## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/financial-risk-profiler.git
   cd financial-risk-profiler
