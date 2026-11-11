import numpy as np

TRADING_DAYS = 252

def total_return(equity):
    return equity.iloc[-1] / equity.iloc[0] - 1

def annualized_return(equity):
    years = len(equity) / TRADING_DAYS
    return (equity.iloc[-1] / equity.iloc[0]) ** (1 / years) - 1

def max_drawdown(equity):
    running_peak = equity.cummax()
    drawdown = equity / running_peak - 1
    return drawdown.min()

def sharpe_ratio(equity, risk_free_rate=0.0):
    daily_returns = equity.pct_change().dropna()
    excess = daily_returns - risk_free_rate / TRADING_DAYS
    return excess.mean() / excess.std() * np.sqrt(TRADING_DAYS)

def summarize(equity):
    return {
        "Final Value": f"${equity.iloc[-1]:,.0f}",
        "Total Return": f"{total_return(equity):.1%}",
        "Annual Return": f"{annualized_return(equity):.1%}",
        "Max Drawdown": f"{max_drawdown(equity):.1%}",
        "Sharpe Ratio": f"{sharpe_ratio(equity):.2f}",
        "Trades": equity.attrs.get("trades", "n/a"),
    }