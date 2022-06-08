import pandas as pd
import datetime as dt
from random import randint

contact_list = pd.read_csv('birthdays.csv')
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day


def check_birthday_list():
    current_month_list = contact_list[contact_list['month'] == current_month]
    birthday_list = current_month_list[current_month_list['day'] == current_day].to_dict(orient="records")
    return birthday_list


def pick_template():
    with open(f'letter_templates/letter_{randint(1,3)}.txt') as file_template:
        letter = file_template.read()
        final_template = letter
    return final_template
