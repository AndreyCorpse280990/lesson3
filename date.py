from datetime import datetime, timedelta, date
dt_now = date.today()

one_day = timedelta(days=1)
yesterday_date = dt_now - one_day
print(yesterday_date)
print(dt_now)

month_delta = timedelta(days=30)
month_date = dt_now - month_delta
print(month_date)

