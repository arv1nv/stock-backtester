import numpy as np
import pandas as pd
import pytest

from src.engine import buy_and_hold, run_backtest
from src.strategies import MovingAverageCrossover, RSIMeanReversion
from src.metrics import total_return, max_drawdown


def make_prices(closes):
    dates = pd.date_range("2020-01-01", periods=len(closes), freq="B")
    return pd.DataFrame({"Open": closes, "Close": closes}, index=dates)


class AlwaysInvested:
    name = "Always Invested"
    def generate_signals(self, prices):
        return pd.Series(1, index=prices.index)


class LastDayOnly:
    name = "Last Day Only"
    def generate_signals(self, prices):
        signals = pd.Series(0, index=prices.index)
        signals.iloc[-1] = 1
        return signals


# ---------- Engine ----------

def test_buy_and_hold_grows_with_price():
    prices = make_prices([10, 20, 30])
    equity = buy_and_hold(prices, starting_cash=1000)
    assert equity.iloc[-1] == 3000


def test_engine_buys_at_next_day_open():
    prices = make_prices([10, 20, 30])
    equity = run_backtest(prices, AlwaysInvested(), starting_cash=1000)
    assert equity.iloc[-1] == 1500
    assert equity.attrs["trades"] == 1


def test_no_look_ahead():
    prices = make_prices([10, 20, 30])
    equity = run_backtest(prices, LastDayOnly(), starting_cash=1000)
    assert equity.attrs["trades"] == 0
    assert equity.iloc[-1] == 1000


def test_fees_reduce_returns():
    prices = make_prices([10, 20, 30])
    no_fee = run_backtest(prices, AlwaysInvested(), starting_cash=1000)
    with_fee = run_backtest(prices, AlwaysInvested(), starting_cash=1000, fee_rate=0.01)
    assert with_fee.iloc[-1] < no_fee.iloc[-1]


# ---------- Metrics ----------

def test_total_return():
    assert total_return(pd.Series([100, 150])) == pytest.approx(0.5)


def test_max_drawdown():
    equity = pd.Series([100, 120, 90, 110])
    assert max_drawdown(equity) == pytest.approx(-0.25)


# ---------- Strategies ----------

def test_ma_crossover_waits_for_long_window():
    prices = make_prices(list(range(1, 101)))
    signals = MovingAverageCrossover(5, 20).generate_signals(prices)
    assert signals.iloc[:19].sum() == 0
    assert signals.iloc[-1] == 1


def test_rsi_stays_between_0_and_100():
    rng = np.random.default_rng(0)
    closes = 100 + rng.normal(0, 1, 300).cumsum()
    rsi = RSIMeanReversion().calculate_rsi(make_prices(closes)).dropna()
    assert rsi.between(0, 100).all()