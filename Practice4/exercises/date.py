from datetime import datetime, timedelta
now = datetime.now()
print("Current datetime:", now)
#1
five_ago = now - timedelta(days=5)
print("Five days ago:", five_ago)
#2
today = now.date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("\nYesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#3
no_micro = now.replace(microsecond=0)
print("\nWithout microseconds:", no_micro)
#4
date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 18, 10, 30, 0)
seconds_diff = (date1 - date2).total_seconds()
print("\nDifference in seconds:", seconds_diff)