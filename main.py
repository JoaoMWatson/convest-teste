import os
import requests
from dotenv import load_dotenv
from pandas.core.frame import DataFrame
from requests.exceptions import HTTPError
from connection import create_connection
from alpha_vantage.timeseries import TimeSeries

load_dotenv()
APIKEY: str = os.getenv('API_TOKEN')


def get_api_data(symbol: str) -> DataFrame:
    ts: TimeSeries = TimeSeries(key=APIKEY, output_format='json')
    data: DataFrame = ts.get_daily(symbol=symbol, outputsize='full')

    return data


if __name__ == '__main__':
    options = ['B3SA3.SAO', 'PETR4.SAO']

    result = get_api_data(options[1])
    print(result)
