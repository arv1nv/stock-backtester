import os
import pandas as pd
import yfinance as yf

DATA_DIR = "data"

def get_prices(ticker, start, end):
    path = os.path.join(DATA_DIR, f"{ticker}_{start}_{end}.csv")

    if os.path.exists(path):
        return pd.read_csv(path, index_col=0, parse_dates=True)

    df = yf.Ticker(ticker).history(start=start, end=end)
    df = df[["Open", "High", "Low", "Close", "Volume"]]

    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(path)
    return df