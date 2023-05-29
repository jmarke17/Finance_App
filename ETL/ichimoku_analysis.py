import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def download_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Descarga los datos del stock especificado."""
    data = yf.download(ticker, start=start, end=end)
    return data

def calculate_ichimoku(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula los valores de Ichimoku Kinko Hyo."""
    high_9 = data['High'].rolling(window=9).max()
    low_9 = data['Low'].rolling(window=9).min()
    data['Tenkan_Sen'] = (high_9 + low_9) / 2

    high_26 = data['High'].rolling(window=26).max()
    low_26 = data['Low'].rolling(window=26).min()
    data['Kijun_Sen'] = (high_26 + low_26) / 2

    data['Senkou_Span_A'] = ((data['Tenkan_Sen'] + data['Kijun_Sen']) / 2).shift(26)
    data['Senkou_Span_B'] = ((data['High'].rolling(window=52).max() + data['Low'].rolling(window=52).min()) / 2).shift(26)

    data['Chikou_Span'] = data['Close'].shift(-26)

    return data

def calculate_signals(data: pd.DataFrame) -> pd.DataFrame:
    """Calcula las señales de compra y venta."""
    # Señal de Compra: Tenkan Sen cruza Kijun Sen de abajo hacia arriba
    data['Buy_Signal'] = np.where((data['Tenkan_Sen'].shift(1) < data['Kijun_Sen'].shift(1)) &
                                  (data['Tenkan_Sen'] > data['Kijun_Sen']), 1, 0)

    # Señal de Venta: Tenkan Sen cruza Kijun Sen de arriba hacia abajo
    data['Sell_Signal'] = np.where((data['Tenkan_Sen'].shift(1) > data['Kijun_Sen'].shift(1)) &
                                   (data['Tenkan_Sen'] < data['Kijun_Sen']), 1, 0)

    return data

def plot_signals(data: pd.DataFrame, ticker: str):
    """Grafica las señales de compra y venta junto con Ichimoku Kinko Hyo."""
    plt.figure(figsize=(10, 5))

    # Gráficas originales
    plt.plot(data.index, data['Close'], color='black', label='Close')
    plt.plot(data.index, data['Tenkan_Sen'], color='blue', label='Tenkan Sen')
    plt.plot(data.index, data['Kijun_Sen'], color='red', label='Kijun Sen')
    plt.plot(data.index, data['Senkou_Span_A'], color='green', label='Senkou Span A')
    plt.plot(data.index, data['Senkou_Span_B'], color='yellow', label='Senkou Span B')
    plt.plot(data.index, data['Chikou_Span'], color='purple', label='Chikou Span')

    # Señales de Compra y Venta
    plt.plot(data[data['Buy_Signal'] == 1].index, data['Tenkan_Sen'][data['Buy_Signal'] == 1], '^', markersize=10,
             color='g', label='buy')
    plt.plot(data[data['Sell_Signal'] == 1].index, data['Tenkan_Sen'][data['Sell_Signal'] == 1], 'v', markersize=10,
             color='r', label='sell')

    plt.fill_between(data.index, data['Senkou_Span_A'], data['Senkou_Span_B'], color='lightgrey', alpha=0.3)
    plt.title(f"Ichimoku Kinko Hyo: {ticker}")
    plt.legend()
    plt.grid()
    plt.show()


# Ejemplo de uso
data = download_stock_data('AAPL', '2020-01-01', '2023-01-01')
data_with_ichimoku = calculate_ichimoku(data)
data_with_signals = calculate_signals(data_with_ichimoku)
plot_signals(data_with_signals, 'AAPL')