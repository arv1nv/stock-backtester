from src.data_loader import get_prices

df = get_prices("AAPL", "2015-01-01", "2025-01-01")
print(df.head())
print(len(df), "trading days")