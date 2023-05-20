import yfinance as yf
from functools import wraps
from pandas.core.frame import DataFrame

class DataLoader:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def error_handler(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print(f"Error occurred in function {func.__name__} with arguments {args} {kwargs}: {e}")
        return wrapper

    @error_handler
    def load_data(self):
        print(f"Attempting to load data for {self.ticker} from {self.start_date} to {self.end_date}")
        try:
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            print(data)
        except Exception as e:
            print(f"Error occurred while fetching data: {e}")
            return None

        if not isinstance(data, DataFrame):
            print(f"Data loaded for {self.ticker} is not a DataFrame. Returning None.")
            return None

        return data
