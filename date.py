from datetime import datetime, timedelta, date
dt_now = date.today()

one_day = timedelta(days=1)
yesterday_date = dt_now - one_day
print(yesterday_date)
print(dt_now)
month_delta = timedelta(days=30)
month_date = dt_now - month_delta
print(month_date)

date_srt = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(date_srt, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
