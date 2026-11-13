import pandas as pd
import matplotlib.pyplot as plt
from src.data_loader import get_prices
from src.engine import buy_and_hold, run_backtest
from src.strategies import MovingAverageCrossover, RSIMeanReversion
from src.metrics import summarize

df = get_prices("AAPL", "2015-01-01", "2025-01-01")

FEE = 0.001  # 0.1% per trade

results = [
    buy_and_hold(df, fee_rate=FEE),
    run_backtest(df, MovingAverageCrossover(50, 200), fee_rate=FEE),
    run_backtest(df, RSIMeanReversion(), fee_rate=FEE),
]

summary = pd.DataFrame({equity.name: summarize(equity) for equity in results})
print(summary)

pd.concat(results, axis=1).plot(title="AAPL Strategy Comparison", ylabel="Portfolio Value ($)")
plt.show()