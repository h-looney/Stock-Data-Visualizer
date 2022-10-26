from helpers import valid_input, valid_date_input, str_to_date, print_list
from StockDataChart import StockDataChart, CHART_TYPES, TIME_SERIES


def gen_stock_data():
    print("Data Stock Visualizer")
    print("---------------------\n")
    while True:
        try:
            # Stock Symbol
            symbol = input('Enter the stock symbol you are looking for: ')
            # Chart Type
            print_list(CHART_TYPES, 'Available Chart Types')
            chart_type = valid_input('Choose a chart type to generate:', 'That chart type is invalid.', lambda v: v in CHART_TYPES)
            # Time Series
            print_list(TIME_SERIES, 'Available Time Series Options')
            time_series = valid_input('Choose a time series option:', 'That time series option is invalid.', lambda v: v in TIME_SERIES)
            # Start Date
            print()
            start_date = valid_date_input('Enter the start date (YYYY-MM-DD):', 'Must be a valid date (YYYY-MM-DD).')
            # End Date
            print()
            end_date = valid_date_input('Enter the end date (YYYY-MM-DD):', 'Must be a valid date (YYYY-MM-DD) after the start date.', lambda v: str_to_date(v) > start_date)
            break
        except ValueError:
            print("Error: Invalid number. Please enter a new value: ")
    chart = StockDataChart(symbol, time_series, start_date, end_date)
    chart.render(chart_type)
    if input('\nWould you like to view more stock data? (y/n) ') == 'y':
        print()
        gen_stock_data()
    else:
        print('\nGoodbye.')


gen_stock_data()
