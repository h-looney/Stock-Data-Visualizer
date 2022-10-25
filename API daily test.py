from sqlite3 import Date
from tokenize import Double
import requests
import pygal
from datetime import datetime, timedelta
import json

##pulled from documentation for reference with API in use
#initialize variables
symbol = "IBM"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=5min&apikey=AU4UXQO6WFYENR4J'
r = requests.get(url)
data = r.json()
i = 0
Highinput = []
Openinput = []
Lowinput = []
Closeinput = []
DateArray = []
open, high, low, close = "OPEN", "HIGH", "LOW","CLOSE"

UserStartDate = '2021-10-20'
UserEndDate = '2022-10-20'


#creates a datetime object using a string
date_1s = datetime.strptime(UserStartDate, '%Y-%m-%d') 
date_2s = datetime.strptime(UserEndDate, '%Y-%m-%d')

#iterate through the range of user input, and add increment
#through the day by one until the end date equals the start
while date_2s != date_1s:
    
    #converts the object back to a string
    date_1 = date_1s.strftime('%Y-%m-%d')
    date_2 = date_2s.strftime('%Y-%m-%d')
    dt = date_1
    DateArray.append(dt)
    date_1s += timedelta(days=1)
    
    #There is a key error for every day that doesn't exist, 
    #to combat this we continue through the 
    #iteration even if there's no value for the associated key
    try:
        opendata = data['Time Series (Daily)'][dt]['1. open']
        highdata = data['Time Series (Daily)'][dt]['2. high']
        lowdata = data['Time Series (Daily)'][dt]['3. low']
        closedata = data['Time Series (Daily)'][dt]['4. close']
        #print(highdata,opendata,lowdata,closedata)

        
    except KeyError:
        if KeyError:
            #print(dt)
            DateArray.remove(dt)
            #print(DateArray)
            
            continue
        
        
    #create arrays to be used for values in pygal
    
    Highinput.append(highdata)
    Closeinput.append(closedata)
    Lowinput.append(lowdata)
    Openinput.append(opendata)
    #print(Highinput)

    #data in arrays must be converted in float to be listed on graph
    newlist = [float(x) for x in Highinput]
    newlist2 = [float(x) for x in Openinput]
    newlist3 = [float(x) for x in Lowinput]
    newlist4 = [float(x) for x in Closeinput]
    #newlist5 = [(x) for x in DateArray]


chart = pygal.Line(x_label_rotation= 45, title=f'{symbol} stocks for {UserStartDate} - {UserEndDate}')
chart.x_labels = DateArray
chart.add(high,newlist)
chart.add(low, newlist3)
chart.add(open,newlist2)
chart.add(close, newlist4)
#print(Highinput)
#print(DateArray)

chart.render_in_browser()
