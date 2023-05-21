import unittest
from unittest.mock import Mock
from datetime import datetime
import pandas as pd


class TestDataValidation(unittest.TestCase):

    def setUp(self):
        # Mock the DataLoader class
        self.mock_data_loader = Mock()

    def test_no_null_values(self):
        # Set up a dummy dataframe for testing
        dummy_data = pd.DataFrame({
            'Close': [10, 20, 30, 20, 40]
        }, index=pd.date_range(start='1/1/2020', periods=5))

        # Configure the mock to return the dummy dataframe
        self.mock_data_loader.load_data.return_value = dummy_data

        # Assert that there are no null values in the data
        self.assertFalse(dummy_data.isnull().values.any())

    def test_only_integers(self):
        # Set up a dummy dataframe for testing
        dummy_data = pd.DataFrame({
            'Close': [10, 20, 30, 20, 40]
        }, index=pd.date_range(start='1/1/2020', periods=5))

        # Configure the mock to return the dummy dataframe
        self.mock_data_loader.load_data.return_value = dummy_data

        # Assert that all values in the 'Close' column are integers
        self.assertTrue(dummy_data['Close'].apply(lambda x: isinstance(x, int)).all())


if __name__ == '__main__':
    unittest.main()