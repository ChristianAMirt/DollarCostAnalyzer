import sys

#from IntervalAnalyzer import IntervalAnalyzer
from StockBuilder import StockBuilder


def main():
    test_stock = StockBuilder('SPY', "2023-01-13")

    print(test_stock)

if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as err:
        print(err)