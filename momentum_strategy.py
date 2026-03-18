# IMPORTS
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# DATA
stocks = pd.read_csv("constituents.csv")

tickers = stocks["Symbol"].tolist()
tickers = [t.replace(".", "-") for t in tickers]
print(tickers[:10])
tickers = tickers[:150]
print(f"total stocks: {len(tickers)}")

prices= yf.download(tickers, start="2008-01-01", end="2018-01-01", auto_adjust= True)["Close"]
print(prices.head())
print(prices.tail())

prices = prices.dropna(axis=1, thresh=1000)
prices = prices.ffill()
prices = prices.dropna()
print(len(prices))

# RETURNS
returns = prices.pct_change().dropna()

# MOMENTUM
window= 126
momentum = prices.shift(21).pct_change(126)
print(momentum.head())
print(momentum.tail())

# RANKING
ranks = momentum.rank(axis=1, ascending=False)
percentile = momentum.rank(axis=1, pct=True)

print(ranks.head())
print(percentile.head())

# SIGNALS
winners = percentile >= 0.99
losers = percentile <= 0.01

# POSITIONS
positions = pd.DataFrame(0, index=momentum.index, columns=momentum.columns)
positions[winners] = 1
positions[losers] = -1
positions = positions.div(positions.abs().sum(axis=1), axis=0)
positions = positions.shift(1)

# STRATEGY RETURNS
strategy_returns = (positions * returns).sum(axis=1)

# PERFORMANCE
equity_curve = (1 + strategy_returns).cumprod()

sharpe = np.sqrt(252) * strategy_returns.mean() / strategy_returns.std()
print("Sharpe Ratio:", sharpe)

rolling_max = equity_curve.cummax()
drawdown = (equity_curve - rolling_max) / rolling_max
max_dd = drawdown.min()

print("Max Drawdown:", max_dd)

# PLOT
equity_curve.plot(figsize=(10,5))
plt.title("Momentum Strategy Equity Curve")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.show()
