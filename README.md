# Stock Backtester

A Python tool that tests trading strategies on historical stock prices to see how they would have performed.

## Example: Apple (AAPL), 2015 to 2024

Each strategy started with $10,000 and paid a 0.1% fee per trade.

| Metric | Buy and Hold | MA Crossover (50/200) | RSI (14, 30/70) |
| --- | --- | --- | --- |
| Final Value | $102,685 | $49,375 | $37,306 |
| Total Return | 927.9% | 393.7% | 273.1% |
| Annual Return | 26.3% | 17.3% | 14.1% |
| Max Drawdown | -38.5% | -45.9% | -28.6% |
| Sharpe Ratio | 0.96 | 0.80 | 0.76 |
| Trades | 1 | 9 | 24 |

![Strategy comparison](results/equity_curve.png)

## Getting started

```bash
git clone https://github.com/arv1nv/stock-backtester.git
cd stock-backtester
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

To try a different stock or time period, change the ticker and dates in `main.py`.

To run the tests:

```bash
python -m pytest
```
