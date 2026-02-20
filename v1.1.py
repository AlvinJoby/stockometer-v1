# Stock_Analyzer Version-1.0

import pandas as pd

def load_data(file_path):

    """Load stock data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("\nData loaded successfully.")
        return data
    except Exception as e:
        print(f"\nError loading data: {e}")
        return None


def examine_csv(data):

    """Examine the structure of the CSV data."""
    if data is not None:
        print("\nCSV - Architectural Overview:")
        print("\nShape of the data:", data.shape)
        print("\nData types of each column:", data.dtypes)
        print("\nNumber of columns:", len(data.columns))
        print("\nNumber of rows:", len(data))
        
    else:
        print("No data to examine.")

def preprocess_data(data):

    """Preprocess the data for analysis."""
    print("Preprocessing data...")

    data['DATE'] = pd.to_datetime(data['DATE'])
    data = data.sort_values('DATE',ascending=True)
    data = data.set_index("DATE")

    numeric_columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'NO. OF TRADES']

    for col in numeric_columns:
        data[col] = data[col].astype(str).str.replace(',', '')
        data[col] = pd.to_numeric(data[col], errors='coerce')

    
    return data

def analyze_data(data):
    """Perform basic analysis on the stock data."""
    print("\nAnalyzing data...")
    print("\nSummary statistics:")
    print(data.describe())

def daily_returns(data):
    """Calculate daily returns."""
    data['Daily Return'] = data['CLOSE'].pct_change()
    print("\nAbout Daily Returns:")
    print("\nHighest Daily Return: ", data['Daily Return'].max())
    print("Lowest Daily Return: ", data['Daily Return'].min())
    print("Average Daily Return: ", data['Daily Return'].mean())
    return data

def voltality(data):
    """Calculate volatility."""
    data['Volatility'] = data['CLOSE'].rolling(window=30).std()
    print("\nAbout Volatility:")
    print("\nHighest Volatility: ", data['Volatility'].max())
    print("Lowest Volatility: ", data['Volatility'].min())
    print("Average Volatility: ", data['Volatility'].mean())
    
    return data

def main():
    data = load_data('reliance.csv')

    if data is not None:
        data = preprocess_data(data)
        examine_csv(data)
        analyze_data(data)
        daily_returns(data)
        voltality(data)



if __name__ == "__main__":
    main()


