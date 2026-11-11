import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import get_prices
from src.engine import buy_and_hold, run_backtest
from src.strategies import MovingAverageCrossover

df = get_prices("AAPL", "2015-01-01", "2025-01-01")

results = [
    buy_and_hold(df),
    run_backtest(df, MovingAverageCrossover(50, 200)),
]

for equity in results:
    print(f"{equity.name:<25} ${equity.iloc[-1]:,.2f}")

pd.concat(results, axis=1).plot(title="AAPL Strategy Comparison", ylabel="Portfolio Value ($)")
plt.show()