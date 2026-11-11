import pandas as pd

def buy_and_hold(prices, starting_cash=10_000):
    first_price = prices["Close"].iloc[0]

    shares = starting_cash // first_price
    leftover_cash = starting_cash - shares * first_price

    portfolio_value = shares * prices["Close"] + leftover_cash
    portfolio_value.name = "Buy and Hold"

    return portfolio_value