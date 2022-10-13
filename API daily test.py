import requests

##pulled from documentation for reference with API in use
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey=AU4UXQO6WFYENR4J'
r = requests.get(url)
data = r.json()

print(data)

