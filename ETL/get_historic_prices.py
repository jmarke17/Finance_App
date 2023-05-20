import pandas_datareader as pdr
import datetime
from functools import wraps

class DataLoader:
    def __init__(self, ticker, start_date, end_date):
        # Initialize DataLoader with ticker symbol and start and end dates
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    # Decorator for handling potential errors
    def error_handler(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                # Try executing the function
                return func(self, *args, **kwargs)
            except Exception as e:
                # If error occurs, print it
                print(f"Error occurred: {e}")
        return wrapper

    # Method using decorator for error handling
    @error_handler
    def load_data(self):
        # Load data using pandas_datareader's get_data_yahoo method
        data = pdr.get_data_yahoo(self.ticker, self.start_date, self.end_date)
        return data
