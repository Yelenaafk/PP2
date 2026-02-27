import datetime

x = datetime.datetime(2018, 6, 1)
y = datetime.datetime(2022, 8, 3)
print(x.strftime(y - x))