# Cross-Sectional Momentum Strategy

## Overview
This project implements a cross-sectional momentum strategy across a large universe of stocks.

The strategy ranks stocks based on past returns and takes long positions in top performers and short positions in worst performers.

## Methodology

### 1. Data Collection
- Stock universe imported from S&P 500 constituents
- Historical price data from yFinance
- Time period: 2008–2018
- Universe size: ~150 stocks

### 2. Data Preprocessing
- Removed stocks with insufficient data
- Forward-filled missing values
- Computed daily returns

### 3. Momentum Calculation
- Lookback period: 126 days (~6 months)
- Skip period: 21 days (~1 month)
- Momentum = return from t-126 to t-21

### 4. Ranking & Portfolio Construction
- Stocks ranked cross-sectionally each day
- Top 1% → Long positions
- Bottom 1% → Short positions
- Positions normalized to maintain equal weighting
- Signals shifted to avoid lookahead bias

### 5. Backtesting
- Portfolio returns computed daily
- Strategy equity curve generated

## Performance Metrics
- Sharpe Ratio: 1.158
- Max Drawdown: -0.256

## Key Insights
- Momentum effect persists across a broad universe of stocks
- Cross-sectional ranking captures relative strength effectively
- Extreme percentile selection improves signal strength
- Diversification across many stocks reduces idiosyncratic risk

## Tools Used
- Python
- Pandas
- NumPy
- yFinance
- Matplotlib

## Future Improvements
- Add transaction costs and turnover analysis
- Use volatility scaling
- Test different percentile thresholds
- Expand to global markets
