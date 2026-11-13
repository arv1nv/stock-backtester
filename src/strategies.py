import numpy as np
import pandas as pd

class MovingAverageCrossover:
    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window
        self.name = f"MA Crossover ({short_window}/{long_window})"

    def generate_signals(self, prices):
        short_ma = prices["Close"].rolling(self.short_window).mean()
        long_ma = prices["Close"].rolling(self.long_window).mean()
        signals = (short_ma > long_ma).astype(int)
        return signals

class RSIMeanReversion:
    def __init__(self, period=14, oversold=30, overbought=70):
        self.period = period
        self.oversold = oversold
        self.overbought = overbought
        self.name = f"RSI ({period}, {oversold}/{overbought})"

    def calculate_rsi(self, prices):
        change = prices["Close"].diff()
        gains = change.clip(lower=0)
        losses = -change.clip(upper=0)

        avg_gain = gains.ewm(alpha=1 / self.period, adjust=False).mean()
        avg_loss = losses.ewm(alpha=1 / self.period, adjust=False).mean()

        rs = avg_gain / avg_loss
        return 100 - 100 / (1 + rs)

    def generate_signals(self, prices):
        rsi = self.calculate_rsi(prices)

        signals = pd.Series(np.nan, index=prices.index)
        signals[rsi < self.oversold] = 1
        signals[rsi > self.overbought] = 0

        return signals.ffill().fillna(0).astype(int)