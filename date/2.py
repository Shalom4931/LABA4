from datetime import date, datetime, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomrow = today + timedelta(days=1)
print (today , yesterday , tomrow)
