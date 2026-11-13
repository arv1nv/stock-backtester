import pandas as pd

def buy_and_hold(prices, starting_cash=10_000, fee_rate=0.0):
    first_price = prices["Close"].iloc[0]
    cost_per_share = first_price * (1 + fee_rate)

    shares = starting_cash // cost_per_share
    leftover_cash = starting_cash - shares * cost_per_share

    portfolio_value = shares * prices["Close"] + leftover_cash
    portfolio_value.name = "Buy and Hold"
    portfolio_value.attrs["trades"] = 1

    return portfolio_value



def run_backtest(prices, strategy, starting_cash=10_000, fee_rate=0.0):
    signals = strategy.generate_signals(prices)

    cash = starting_cash
    shares = 0
    trades = 0
    values = []

    for i in range(len(prices)):
        if i > 0:
            signal = signals.iloc[i - 1]
            open_price = prices["Open"].iloc[i]

            if signal == 1 and shares == 0:
                shares = cash // (open_price * (1 + fee_rate))
                cash -= shares * open_price * (1 + fee_rate)
                trades += 1

            elif signal == 0 and shares > 0:
                cash += shares * open_price * (1 - fee_rate)
                shares = 0
                trades += 1

        close_price = prices["Close"].iloc[i]
        values.append(cash + shares * close_price)

    equity = pd.Series(values, index=prices.index, name=strategy.name)
    equity.attrs["trades"] = trades
    return equity