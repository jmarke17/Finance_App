import datetime
from get_historic_prices import DataLoader

def main():
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime(2023, 5, 20)

    bitcoin_loader = DataLoader('BTC-USD', start_date, end_date)
    bitcoin_data = bitcoin_loader.load_data()
    print(bitcoin_data)

    apple_loader = DataLoader('AAPL', start_date, end_date)
    apple_data = apple_loader.load_data()
    print(apple_data)

if __name__ == "__main__":
    main()