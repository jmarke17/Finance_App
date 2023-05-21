from ETL.get_historic_prices import DataLoader
from ETL.graphic import DataPlotter
from Utils.constants import START_DATE,END_DATE,tickers

def process_ticker(ticker):
    loader = DataLoader(ticker, START_DATE, END_DATE)
    data = loader.load_data()
    print(data)
    plotter = DataPlotter(loader)
    plotter.plot_data()

def main():
    for ticker in tickers:
        process_ticker(ticker)

if __name__ == "__main__":
    main()