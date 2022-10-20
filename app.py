from helpers import valid_input, valid_date_input, str_to_date, print_list

CHART_TYPES = ['Bar', 'Line']
TIME_SERIES_OPTS = ['Intraday', 'Daily', 'Weekly', 'Monthly']

print("Data Stock Visualizer")
print("---------------------\n")
# Stock Symbol
symbol = input('Enter the stock symbol you are looking for: ')
# Chart Type
print_list(CHART_TYPES, 'Available Chart Types')
chart_type = valid_input('Choose a chart type to generate:', 'That chart type is invalid.', lambda v: v in CHART_TYPES)
# Time Series
print_list(TIME_SERIES_OPTS, 'Available Time Series Options')
time_series = valid_input('Choose a time series option:', 'That time series option is invalid.', lambda v: v in TIME_SERIES_OPTS)
# Start Date
print()
start_date = valid_date_input('Enter the start date (YYYY-MM-DD):', 'Must be a valid date (YYYY-MM-DD).')
# End Date
print()
end_date = valid_date_input('Enter the end date (YYYY-MM-DD):', 'Must be a valid date (YYYY-MM-DD) after the start date.', lambda v: str_to_date(v) > start_date)
