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

