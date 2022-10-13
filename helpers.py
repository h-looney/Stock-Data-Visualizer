from datetime import datetime

DF_DEFAULT = '%Y-%m-%d'


def str_to_date(v, f=DF_DEFAULT):
    return datetime.strptime(v, f)


def is_valid_date(v):
    try:
        str_to_date(v)
    except ValueError:
        return False
    else:
        return True


def valid_input(prompt, error_msg, validator):
    user_input = input(f'{prompt} ')
    while not validator(user_input):
        print(f'{error_msg} Please try again.')
        user_input = input(f'{prompt} ')
    return user_input


def valid_date_input(prompt, error_msg, validator=lambda v: True):
    date_str = valid_input(prompt, error_msg, lambda v: is_valid_date(v) and validator(v))
    return str_to_date(date_str)
