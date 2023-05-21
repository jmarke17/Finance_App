import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from Utils.constants import TICKERS, START_DATE, END_DATE

def calculate_financial_ratios(df):
    # Here you would calculate the financial ratios you're interested in
    # For example, the net income ratio:
    df['NetIncomeRatio'] = df['NetIncome'] / df['TotalRevenue']
    return df

def plot_financial_ratios(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=df.index, y='NetIncomeRatio')
    plt.title("Net Income Ratio over time")
    plt.show()

def analyze_financials(ticker):
    try:
        # Create a Ticker object
        ticker_info = yf.Ticker(ticker)

        # Check if the ticker represents a company
        if 'sector' in ticker_info.info:
            # Download the balance sheet data
            balance_sheet_df = ticker_info.balancesheet

            # Calculate financial ratios
            df = calculate_financial_ratios(balance_sheet_df)

            # Plot the financial ratios
            plot_financial_ratios(df)
        else:
            print(f"{ticker} does not represent a company. Skipping...")
    except Exception as e:
        print(f"Failed to analyze financials for {ticker}. Error: {e}")

##TODO recalcular para pandas data-reader