import requests
import json

#Will be used to stop data if no date is provided
DEFAULT_DATE = "2004-01-14"

class StockBuilder:
    """
    Sends requests to AlphaVantage API and processes response into Stock object
    """
    def __init__(self, ticker: str = "No-Name", date: str = DEFAULT_DATE):
        self._ticker_symbol: str = ticker
        self._end_date_of_data: str = date
        self._json_data: dict = self.read_from_API()


    @property
    def ticker_symbol(self) -> str:
        """
        Get the symbol for the stock
        """
        return self._ticker_symbol
    
    @property
    def end_date_of_data(self) -> str:
        """
        Get end date range of data
        """
        return self._end_date_of_data
    
    
    def read_from_API(self) -> dict:
        """
        Retrives data from stock
        """
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.ticker_symbol}&outputsize=full&apikey=XY1MFHCZCQT2EIN4'
        response = requests.get(url)
        if response.status_code == 200:
            return self._cutoff_date(response.json())
        else: 
            return KeyError
        
    def _cutoff_date(self, raw_data) -> dict:
        """
        Removes any data beyond the given date
        """
        new_data = {}

        for date in raw_data["Time Series (Daily)"]:
            if date <= self._end_date_of_data:
                break
            
            new_data[date] = raw_data["Time Series (Daily)"][date]["1. open"]

        return new_data

    def __str__(self) -> str:
        print(f"Data for the stock ticker: {self._ticker_symbol}", '\n')
        return json.dumps(self._json_data, indent=2)