from datetime import datetime  
from ETL.get_historic_prices import DataLoader  
from ETL.graphic import DataPlotter

START_DATE = datetime(2020, 1, 1)
END_DATE = datetime(2023, 5, 20)

def process_ticker(ticker):
    loader = DataLoader(ticker, START_DATE, END_DATE)
    data = loader.load_data()
    print(data)
    plotter = DataPlotter(loader)
    plotter.plot_data()

def main():
    for ticker in ['BTC-USD', 'AAPL']:
        process_ticker(ticker)

if __name__ == "__main__":
    main()