from ETL.get_historic_prices import DataLoader
from ETL.graphic import DataPlotter
from ETL.financial_analysis import analyze_financials
from ETL.ichimoku_analysis import calculate_ichimoku, calculate_signals, plot_signals
from Utils.constants import START_DATE, END_DATE, TICKERS


def process_ticker(ticker):
    loader = DataLoader(ticker, START_DATE, END_DATE)
    data = loader.load_data()
    print(data)
    plotter = DataPlotter(loader)
    plotter.plot_data()

    # Analyze the financials
    analyze_financials(ticker)

    data_with_ichimoku = calculate_ichimoku(data)
    data_with_signals = calculate_signals(data_with_ichimoku)

    plot_signals(data_with_signals, ticker)

def main():
    for ticker in TICKERS:
        process_ticker(ticker)

if __name__ == "__main__":
    main()