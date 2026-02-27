from datetime import datetime, timezone, timedelta
def parse_datetime_with_tz(s):
    dt_part, tz_part = s.rsplit(' ', 1)
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz_part[3] == '+' else -1
    hours, minutes = map(int, tz_part[4:].split(':'))
    tz_offset = timedelta(hours=hours, minutes=minutes) * sign
    dt = dt.replace(tzinfo=timezone(tz_offset))
    return dt
start = parse_datetime_with_tz(input())
end = parse_datetime_with_tz(input())
start_utc = start.astimezone(timezone.utc)
end_utc = end.astimezone(timezone.utc)
duration_seconds = int((end_utc - start_utc).total_seconds())
print(duration_seconds)