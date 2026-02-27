from datetime import datetime, timedelta
def diff(s):
    date_part, tz_part = s.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if tz_part[3] == '+' else -1
    hours = int(tz_part[4:6])
    minutes = int(tz_part[7:9])
    offset = timedelta(hours=hours, minutes=minutes) * sign
    return dt - offset
dt1 = diff(input().strip())
dt2 = diff(input().strip())
diff_s = abs((dt1 - dt2).total_seconds())
print(int(diff_s // 86400))