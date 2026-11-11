import matplotlib.pyplot as plt
from src.data_loader import get_prices
from src.engine import buy_and_hold

df = get_prices("AAPL", "2015-01-01", "2025-01-01")
equity = buy_and_hold(df)

print(f"Start: ${equity.iloc[0]:,.2f}")
print(f"End:   ${equity.iloc[-1]:,.2f}")
print(f"Portfolio growth: {equity.iloc[-1] / equity.iloc[0]:.2f}x")
print(f"Stock growth:     {df['Close'].iloc[-1] / df['Close'].iloc[0]:.2f}x")

equity.plot(title="AAPL Buy and Hold", ylabel="Portfolio Value ($)")
plt.show()