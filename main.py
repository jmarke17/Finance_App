from ETL.get_historic_prices import DataLoader
from ETL.graphic import DataPlotter
from ETL.financial_analysis import analyze_financials
from Utils.constants import START_DATE, END_DATE, TICKERS

def process_ticker(ticker):
    loader = DataLoader(ticker, START_DATE, END_DATE)
    data = loader.load_data()
    print(data)
    plotter = DataPlotter(loader)
    plotter.plot_data()

    # Analyze the financials
    analyze_financials(ticker)

def main():
    for ticker in TICKERS:
        process_ticker(ticker)

if __name__ == "__main__":
    main()