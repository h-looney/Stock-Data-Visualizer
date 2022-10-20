from tokenize import Double
import requests
import pygal
import json

##pulled from documentation for reference with API in use
symbol = "IBM"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey=AU4UXQO6WFYENR4J'
r = requests.get(url)
data = r.json()

dates, open, high, low, close = [], "OPEN", "HIGH", "LOW","CLOSE"


#datess = input("start date YYYY-MM-DD")
#datee = input ("End date YYYY-MM-DD")
key = data['Time Series (Daily)']
print(key)
###CODE FOR DAILY SERIES
opendata = data['Time Series (Daily)']['2022-10-13']['1. open']
highdata = data['Time Series (Daily)']['2022-10-13']['2. high']
lowdata = data['Time Series (Daily)']['2022-10-13']['3. low']
closedata = data['Time Series (Daily)']['2022-10-13']['4. close']
print(highdata,opendata,lowdata,closedata)

opendata2 = data['Time Series (Daily)']['2022-10-19']['1. open']
highdata2 = data['Time Series (Daily)']['2022-10-19']['2. high']
lowdata2 = data['Time Series (Daily)']['2022-10-19']['3. low']
closedata2 = data['Time Series (Daily)']['2022-10-19']['4. close']


chart = pygal.Line(title=f'{symbol} stocks for 2022-10-14 - 2022-10-19')
chart.add(close,[int(float(closedata)), int(float(closedata2))])
chart.add(open,[int(float(opendata)), int(float(opendata2))])
chart.add(high,[int(float(highdata)), int(float(highdata2))])
chart.add(low,[int(float(lowdata)), int(float(lowdata2))])
chart.render_in_browser()
