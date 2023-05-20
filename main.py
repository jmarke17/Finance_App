import datetime
from ETL.get_historic_prices import DataLoader
from ETL.graphic import DataPlotter  # Asegúrate de que el path a graphic.py sea correcto

def main():
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime(2023, 5, 20)

    # Descargar y graficar los datos de Bitcoin
    bitcoin_loader = DataLoader('BTC-USD', start_date, end_date)
    bitcoin_data = bitcoin_loader.load_data()
    print(bitcoin_data)
    bitcoin_plotter = DataPlotter(bitcoin_loader)
    bitcoin_plotter.plot_data()

    # Descargar y graficar los datos de Apple
    apple_loader = DataLoader('AAPL', start_date, end_date)
    apple_data = apple_loader.load_data()
    print(apple_data)
    apple_plotter = DataPlotter(apple_loader)
    apple_plotter.plot_data()

if __name__ == "__main__":
    main()
