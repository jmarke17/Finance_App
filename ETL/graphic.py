import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from ETL.get_historic_prices import DataLoader
from Utils.constants import START_DATE, END_DATE


class DataPlotter:
    def __init__(self, data_loader):
        self.data_loader = data_loader

    def rsi(self, df, periods=14, ema=True):
        """
        Returns a pd.Series with the relative strength index.
        """
        close_delta = df['Close'].diff()

        # Make two series: one for lower closes and one for higher closes
        up = close_delta.clip(lower=0)
        down = -1 * close_delta.clip(upper=0)

        if ema == True:
            # Use exponential moving average
            ma_up = up.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
            ma_down = down.ewm(com=periods - 1, adjust=True, min_periods=periods).mean()
        else:
            # Use simple moving average
            ma_up = up.rolling(window=periods, adjust=False).mean()
            ma_down = down.rolling(window=periods, adjust=False).mean()

        rsi = ma_up / ma_down
        rsi = 100 - (100 / (1 + rsi))
        return rsi

    def plot_data(self):
        df = self.data_loader.load_data()
        if df is None:
            raise Exception(f"Failed to load data for {self.data_loader.ticker}")

        # Calculate RSI
        df['RSI'] = self.rsi(df)

        fig, ax = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': [2, 1]})
        fig.set_size_inches(10, 6)

        # Plot closing prices
        sns.lineplot(data=df, x=df.index, y='Close', ax=ax[0])
        ax[0].set_title(f"Closing price and RSI of {self.data_loader.ticker}")

        # Plot RSI
        sns.lineplot(data=df, x=df.index, y='RSI', ax=ax[1])
        ax[1].set_title("RSI")

        plt.show()


if __name__ == "__main__":
    data_loader = DataLoader('BTC-USD', START_DATE, END_DATE)
    data_plotter = DataPlotter(data_loader)
    data_plotter.plot_data()