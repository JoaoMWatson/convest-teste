import os
from rich import print
from datetime import date
from datetime import timedelta
from dotenv import load_dotenv
from connection import create_connection
from alpha_vantage.timeseries import TimeSeries

load_dotenv()
APIKEY: str = os.getenv('API_TOKEN')
today: date = date.today()
last_week: date = date.today() - timedelta(days=7)


def get_last_week(symbol: str) -> list:
    """get data from alpha_vantage api

    Args:
        symbol (str): symbol reference to stock example: B3SA3.SAO/PETR4.SAO

    Returns:
        list: Array contains values from last week about passed stock
    """
    print('Fetching API')
    last_week_values: list[dict[str, str]] = []

    ts: TimeSeries = TimeSeries(key=APIKEY, output_format='json')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')

    for i in range(0, 8):
        try:
            last_week_values.append(
                {str(last_week + timedelta(days=i)): data[str(last_week + timedelta(days=i))]['4. close']})
        except KeyError:
            print('Weekend detected, skipping')

    return last_week_values


def get_all_data(symbol):
    ts = TimeSeries(key=APIKEY, output_format='json')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')

    return data


if __name__ == '__main__':
    stocks: str = ['B3SA3.SAO', 'PETR4.SAO']
    all_result = get_all_data(stocks[0])
    result = get_last_week(stocks[0])

    print(result)
