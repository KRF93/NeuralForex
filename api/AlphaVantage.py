from api import AlphaVantageApiKey
import urllib.request

class AlphaVantage ():
    def __init__(self):
        data = urllib.request.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=demo').read()
        print(data)
        #key = AlphaVantageApiKey.API_KEY
        #print(key)
