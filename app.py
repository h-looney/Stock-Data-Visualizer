from helpers import valid_input, valid_date_input, str_to_date

CHART_TYPES = ['bar', 'line', 'graph']

while True: 
    try: 
        symbol = input('Enter the stock symbol. ')
        chart_type = valid_input('What kind of chart would you like to generate?', 'That chart type is invalid.', lambda v: v in CHART_TYPES)
        start_time = valid_date_input('Enter start date.', 'Must be a valid date (YYYY-MM-DD).')
        end_time = valid_date_input('Enter end date.', 'Must be a valid date (YYYY-MM-DD) after the start date.', lambda v: str_to_date(v) >       start_time)
        break
    except ValueError: 
        print("Error: Invalid number. Please enter a new value: ")
