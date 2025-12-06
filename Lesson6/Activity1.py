from datetime import date, time, datetime
now = datetime.now()
today = date.today()
print("Today's day is", today)
print("Current date and time is", now)
print("Date components:", today.year, today.day, today.month)
