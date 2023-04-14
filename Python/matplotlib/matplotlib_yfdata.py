# yfinance data install
!pip install yfinance --upgrade --no-cache-dir

import yfinance as yf

# Tesla data
TSLA = yf.download("TSLA", start="2019-08-01", end="2023-04-13")
TSLA["Close"]

# Apple data
AAPL = yf.download("AAPL", start="2019-08-01", end="2023-04-13")
AAPL["Close"]

# Compare Tesla and Apple Closing Prices
fig, axs = plt.subplots(figsize=(10, 6))
axs.plot(TSLA["Close"], label = "Tesla")
axs.plot(AAPL["Close"], label = "Apple")
axs.set_title("Compare Tesla and Apple Closing Prices")
axs.set_xlabel("Period (2019-08-01 ~ 2023-04-13)")
axs.set_ylabel("Closing Prices (Dollar)")
axs.legend()
plt.show()

# Comparison of S&P 500 Index and Tesla, S&P 500 Index and Apple Closing Price

# S&P 500 data
SPX = yf.download("^GSPC", start="2019-08-01", end="2023-04-13")
SPX["Close"]

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

axs[0].plot(SPX["Close"], label="S&P500", color="red")
axs[0].plot(AAPL["Close"], label="Apple", color="grey")
axs[0].set_title("S&P 500 Index and Apple Closing Price")
axs[0].set_xlabel("Period (2019-08-01 ~ 2023-04-13)")
axs[0].set_ylabel("Closing Prices (Dollar)")
axs[0].legend()

axs[1].plot(SPX["Close"], label="S&P500", color="red")
axs[1].plot(TSLA["Close"], label = "Tesla", color="skyblue")
axs[1].set_title("S&P 500 Index and Tesla Closing Price")
axs[1].set_xlabel("Period (2019-08-01 ~ 2023-04-13)")
axs[1].set_ylabel("Closing Prices (Dollar)")
axs[1].legend()

plt.show()

# Fixed the chart not being pretty
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))

axs[0, 0].plot(SPX["Close"], label="S&P500", color="red")
axs[0, 0].plot(AAPL["Close"], label="Apple", color="grey")
axs[0, 0].set_title("S&P 500 Index and Apple Closing Price")
axs[0, 0].set_xlabel("Period (2019-08-01 ~ 2023-04-13)")
axs[0, 0].set_ylabel("Closing Prices (Dollar)")
axs[0, 0].legend()

axs[0, 1].plot(SPX["Close"], label="S&P500", color="red")
axs[0, 1].plot(TSLA["Close"], label = "Tesla", color="skyblue")
axs[0, 1].set_title("S&P 500 Index and Tesla Closing Price")
axs[0, 1].set_xlabel("Period (2019-08-01 ~ 2023-04-13)")
axs[0, 1].set_ylabel("Closing Prices (Dollar)")
axs[0, 1].legend()

SPX_A = (SPX["Close"])/AAPL["Close"]
SPX_T = (SPX["Close"])/TSLA["Close"]

axs[1, 0].plot(SPX_A, label="S&P500/Apple", color="red")
axs[1, 0].plot(AAPL["Close"], label="Apple", color="grey")
axs[1, 0].set_title("S&P 500 Index/Apple and Apple Closing Price")
axs[1, 0].set_xlabel("Period (2019-08-01 ~ 2023-04-13)")
axs[1, 0].set_ylabel("Closing Prices (Dollar)")
axs[1, 0].legend()

axs[1, 1].plot(SPX_T, label="S&P500/Tesla", color="red")
axs[1, 1].plot(TSLA["Close"], label = "Tesla", color="skyblue")
axs[1, 1].set_title("S&P 500 Index/Tesla and Tesla Closing Price")
axs[1, 1].set_xlabel("Period (2019-08-01 ~ 2023-04-13)")
axs[1, 1].set_ylabel("Closing Prices (Dollar)")
axs[1, 1].legend()

plt.show()
