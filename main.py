import os
import sqlite3
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))  

def create_database(symbol):
    db_path = os.path.join(script_dir, f"financial_data_{symbol}.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stock_prices (
                        id INTEGER PRIMARY KEY,
                        symbol TEXT,
                        date TEXT,
                        open REAL,
                        high REAL,
                        low REAL,
                        close REAL,
                        volume INTEGER)''')
    conn.commit()
    conn.close()
    return db_path

def fetch_stock_data(symbol, days=30):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date, end=end_date)
    return data

def store_data(symbol, data, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    for index, row in data.iterrows():
        cursor.execute('''INSERT INTO stock_prices (symbol, date, open, high, low, close, volume)
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (symbol, index.strftime('%Y-%m-%d'), row['Open'], row['High'], row['Low'], row['Close'], row['Volume']))
    conn.commit()
    conn.close()

def get_data_for_excel(symbol, db_path):
    conn = sqlite3.connect(db_path)
    query = f"SELECT * FROM stock_prices WHERE symbol = '{symbol}'"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def save_to_excel(symbol, db_path):
    df = get_data_for_excel(symbol, db_path)
    file_path = os.path.join(script_dir, f"{symbol}_financial_data.xlsx")
    df.to_excel(file_path, index=False)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    stock_symbol = input("Enter a stock ticker symbol: ").upper().strip()
    db_path = create_database(stock_symbol)
    print(f"Fetching data for {stock_symbol}...")
    stock_data = fetch_stock_data(stock_symbol)
    store_data(stock_symbol, stock_data, db_path)
    save_to_excel(stock_symbol, db_path)
    print("Process complete!")
