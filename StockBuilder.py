from dataclasses import dataclass
import requests


class StockBuilder:
    """
    Sends requests to AlphaVantage API and processes response into Stock object
    """
    def __init__(self, ticker):

    
    def read_from_API(self):
        """
        Retrives data from stock
        """

    def response_is_valid(self) -> bool:
        """
        Ensures API prodived a valid response or raises exception
        """
    def __iter__(self):
        """
        Interator for daily_Data_Collection
        """
    def __repr__(self):

    @dataclass
    class DailyData:
        """
        Price of stock for a specific date
        """
        date: str
        open_price: float

