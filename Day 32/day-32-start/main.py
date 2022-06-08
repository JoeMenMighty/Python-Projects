import datetime as dt
from random import choice
from gmail_to_ymail import send_from_gmail_ymail

with open('quotes.txt') as quotes_file:
    quotes = quotes_file.readlines()
    # special_quote = "Try quote"
    special_quote = choice(quotes).encode("ascii", "ignore")


current_date = dt.datetime.now()
if current_date.weekday() == 1:
    print("Sending email.........")
    email_msg = f"Subject: Mighty Quotes\n\n{special_quote}"
    send_from_gmail_ymail(email_msg)
    print("Email sent !!!")

