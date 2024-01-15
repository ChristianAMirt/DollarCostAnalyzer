from typing import List
import requests


class StockBuilder:
    """
    Sends requests to AlphaVantage API and processes response into Stock object
    """
    def __init__(self, ticker: str = "No-Name"):
        self._ticker_symbol: str = ticker
        self._json_data: dict = read_from_API()

    @property
    def ticker_symbol(self) -> str:
        """
        Get the symbol for the stock
        """
        return self._ticker_symbol
    
    def read_from_API(self) -> dict:
        """
        Retrives data from stock
        """
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={_ticker_symbol}&outputsize=full&apikey=XY1MFHCZCQT2EIN4'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else: 
            raise ValueError("API Response not Valid")
