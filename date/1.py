from datetime import datetime, timedelta

today = datetime.now().date()

yesterday = today - timedelta(days=5)

print( yesterday)