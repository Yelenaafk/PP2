from datetime import datetime, timezone, timedelta
# Create an aware datetime object in UTC
utc_datetime = datetime(2023, 6, 5, 14, 30, 45, tzinfo=timezone.utc)
print(f"UTC time: {utc_datetime}") # Output: 2023-06-05 14:30:45+00:00
# Define another time zone (e.g., Pacific Time, UTC-8)
pacific_tz = timezone(timedelta(hours=-8), 'Pacific/A_Specific_Location')
# Convert the UTC datetime to Pacific time
pacific_datetime = utc_datetime.astimezone(pacific_tz)
print(f"Pacific time: {pacific_datetime}") # Output: 2023-06-05 06:30:45-08:00