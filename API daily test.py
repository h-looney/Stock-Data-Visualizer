import requests
import pygal

##pulled from documentation for reference with API in use
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey=AU4UXQO6WFYENR4J'
r = requests.get(url)
data = r.json()

#print(data)
dates, open, high, low, close = [], [], [], []


for point in data: 
    dates.append
