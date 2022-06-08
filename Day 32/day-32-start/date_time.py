import datetime as dt

# print current data and time
now = dt.datetime.now()

# print current year, month, day, hour, minutes, seconds, weekday
current_year = now.year
current_month = now.month
current_day = now.day
current_hour = now.hour
current_minute = now.minute
current_weekday = now.weekday()
print(current_month)

# create a Datatime object for birthday
my_birthday = dt.datetime(year=1999, month=4, day=7, hour=4)
print(my_birthday)