#!/usr/bin/python3

import requests
from pprint import pprint

def main():
    mylookup = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=5V0VWGXAZU5GDWX5"
    stockdata = requests.get(mylookup) # this is the initial lookup
    #pprint(stockdata.json())) # display the returned JS
    decodedstockdata = stockdata.json()
    lastrefresh = stockdata.json()["Meta Data"]["3. Last Refreshed"] # pull the latest refresh info
    #pprint(stockdata.json()["Time Series (5min)"][lastrefresh])
    ##print(decodedstockdata["Meta Data"]["3. Last Refreshed"])


    cryptolookup = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=5V0VWGXAZU5GDWX5"
    crypto = requests.get(cryptolookup)
    cryptojson = crypto.json()
    pprint(cryptojson['Realtime Currency Exchange Rate']['2. From_Currency Name'])
    pprint(cryptojson['Realtime Currency Exchange Rate']['4. To_Currency Name'])
    pprint(cryptojson['Realtime Currency Exchange Rate']['5. Exchange Rate'])



main()
