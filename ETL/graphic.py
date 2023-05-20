import seaborn as sns
import matplotlib.pyplot as plt
from ETL.get_historic_prices  import DataLoader
from datetime import datetime

class DataPlotter:
    def __init__(self, data_loader):
        self.data_loader = data_loader

    def plot_data(self):
        # Load the data
        df = self.data_loader.load_data()

        if df is None:
            print(f"Failed to load data for {self.data_loader.ticker}")
            return

        # Plot the data
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x=df.index, y='Close')
        plt.title(f"Closing price of {self.data_loader.ticker}")
        plt.show()

if __name__ == "__main__":
    # Create an instance of DataLoader
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 5, 20)
    data_loader = DataLoader('BTC-USD', start_date, end_date)

    # Create an instance of DataPlotter
    data_plotter = DataPlotter(data_loader)

    # Plot the data
    data_plotter.plot_data()
