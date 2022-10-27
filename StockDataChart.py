import pygal
import requests
from datetime import timedelta
from helpers import date_to_str, DF_DEFAULT, DF_INTRADAY

CHART_TYPES = ['Bar', 'Line']
TIME_SERIES = {
    'Intraday': {'key': '', 'scale': {}},
    'Daily': {'key': 'Time Series (Daily)', 'scale': {'days': 1}},
    'Weekly': {'key': 'Weekly Time Series', 'scale': {'days': 1}},
    'Monthly': {'key': 'Monthly Time Series', 'scale': {'days': 1}}
}


class StockDataChart:

    __apiKey = 'AU4UXQO6WFYENR4J'
    default_opts = {'x_label_rotation': 45}
    url = 'https://www.alphavantage.co/query?'
    data = {}

    def __init__(self, symbol, time_series, start_date, end_date):
        self.symbol = symbol
        self.time_series = time_series
        self.start_date = start_date
        self.end_date = end_date
        self.default_opts['title'] = f'{self.symbol} stocks for {date_to_str(self.start_date)} - {date_to_str(self.end_date)}'
        self.url += f'function=TIME_SERIES_{time_series.upper()}&symbol={symbol}&interval=5min&apikey={self.__apiKey}'
        self.fetch_data()

    def fetch_data(self):
        self.data = requests.get(self.url).json()

    def render(self, chart_type, opts={}):
        opts = self.default_opts | opts
        match chart_type:
            case 'Bar': chart = pygal.Bar(**opts)
            case 'Line': chart = pygal.Line(**opts)
            case _: return
        self.build_chart(chart).render_in_browser()

    def build_chart(self, chart):
        x_labels = []
        points = {'OPEN': [], 'HIGH': [], 'LOW': [], 'CLOSE': []}
        stock_data = self.data[TIME_SERIES[self.time_series]['key']]
        dt = self.start_date
        while dt <= self.end_date:
            date_format = DF_INTRADAY if self.time_series == 'Intraday' else DF_DEFAULT
            date_str = date_to_str(dt, date_format)
            try:
                points['OPEN'].append(float(stock_data[date_str]['1. open']))
                points['HIGH'].append(float(stock_data[date_str]['2. high']))
                points['LOW'].append(float(stock_data[date_str]['3. low']))
                points['CLOSE'].append(float(stock_data[date_str]['4. close']))
            except KeyError:
                continue
            else:
                x_labels.append(date_str)
            finally:
                dt += timedelta(**TIME_SERIES[self.time_series]['scale'])
        chart.x_labels = x_labels
        for line in points:
            chart.add(line, points[line])
        return chart
