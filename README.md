# Stock Data Retrieval and Analysis

## Overview
This Python project fetches historical stock data from Yahoo Finance, stores it in an SQLite database, and exports it to an Excel file for easy analysis. The database filename reflects the stock ticker entered by the user (e.g., `financial_data_AAPL.db`).

## Features
- Fetches stock data for any ticker symbol from Yahoo Finance.
- Stores data in a dynamically named SQLite database.
- Exports data to an Excel file for further analysis.
- Supports historical data retrieval for the last 30 days.

## Installation
1. **Clone the repository**:

```
git clone https://github.com/Seth-Banker/Stock-Data-Retrieval.git
```

2. **Install dependencies**:

```
pip install yfinance pandas openpyxl
```

## Usage
Run the script and enter a stock ticker when prompted:

```
python main.py
```

Example input:
Enter a stock ticker symbol: ```AAPL```
- The script creates `financial_data_AAPL.db` and `AAPL_financial_data.xlsx` in the same folder.

## File Output
- **SQLite Database**: `financial_data_<TICKER>.db`
- **Excel File**: `<TICKER>_financial_data.xlsx`

## Troubleshooting
- If you get `ModuleNotFoundError`, install the required libraries:

```
pip install yfinance pandas openpyxl
```

- If Yahoo Finance returns an empty dataset, check if the ticker symbol is valid.
