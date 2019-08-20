#!/usr/bin/python3

import requests
from pprint import pprint

def main():
    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=5V0VWGXAZU5GDWX5"
    stockdata = requests.get(mylookup)
    #pprint(str(stockdata.json())) # display the returned JS
    decodedstockdata = stockdata.json()
    print(decodedstockdata["Meta Data"]["Time Series (5min)"])


main()
