
import pandas as pd
import matplotlib.pyplot as plt

def test_candlestick():

    # DataFrame to represent opening , closing, high 
    # and low prices of a stock for a week
    stock_prices = pd.DataFrame({'open': [36.5, 37.3, 36.9, 37.4, 37.45, 37.31, 38.01],
                                'close': [37.25, 38.3, 35.9, 38.4, 36.45, 38.31, 39.01],
                                'high': [39.0, 39.5, 39.9, 40.1, 39.7, 40.2, 39.9],
                                'low': [34.2, 34.3, 35.7, 35.9, 36.1, 36.2, 36.3]},
                                index=pd.date_range(
                                "2021-11-10", periods=7, freq="d"))

    plt.figure()

    # "up" dataframe will store the stock_prices 
    # when the closing stock price is greater
    # than or equal to the opening stock prices
    up = stock_prices[stock_prices.close >= stock_prices.open]

    # "down" dataframe will store the stock_prices
    # when the closing stock price is
    # lesser than the opening stock prices
    down = stock_prices[stock_prices.close < stock_prices.open]

    # When the stock prices have decreased, then it
    # will be represented by blue color candlestick
    col1 = 'green'

    # When the stock prices have increased, then it 
    # will be represented by green color candlestick
    col2 = 'red'

    # Setting width of candlestick elements
    width = .3
    width2 = .03

    # ax.plot(x, y, label="sine")
    # ax.plot(x, z, label="cosine")
    # ax.legend(loc="upper right", fontsize=16)
    # leg = ax.get_legend()
    # leg.legend_handles[0].set_color('red')
    # leg.legend_handles[1].set_color('yellow')


    # Plotting up prices of the stock
    plt.bar(up.index, up.close-up.open, width, bottom=up.open, color=col1, label="Positive")
    plt.bar(up.index, up.high-up.close, width2, bottom=up.close, color=col1)
    plt.bar(up.index, up.low-up.open, width2, bottom=up.open, color=col1)

    # Plotting down prices of the stock
    plt.bar(down.index, down.close-down.open, width, bottom=down.open, color=col2, label="Negative")
    plt.bar(down.index, down.high-down.open, width2, bottom=down.open, color=col2)
    plt.bar(down.index, down.low-down.close, width2, bottom=down.close, color=col2)

    plt.legend(loc="lower right", fontsize=12)

    # rotating the x-axis tick labels at 30degree 
    # towards right
    plt.xticks(rotation=30, ha='right')

    # displaying candlestick chart of stock data 
    # of a week
    plt.show()

def main():
    test_candlestick()

if __name__ == "__main__":
    main()
