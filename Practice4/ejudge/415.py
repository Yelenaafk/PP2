import datetime
def solve():
    try:
        bl = input().strip()
        cl = input().strip()
    except EOFError:
        return
    def parse_to_utc(line):
        parts = line.split()
        date_str = parts[0]
        offstr = parts[1][3:]
        y, m, d = map(int, date_str.split('-'))
        lmid = datetime.datetime(y, m, d)
        sign = 1 if offstr[0] == '+' else -1
        h, mins = map(int, offstr[1:].split(':'))
        offdelt = datetime.timedelta(hours=h, minutes=mins)
        if sign == 1:
            utc_dt = lmid - offdelt
        else:
            utc_dt = lmid + offdelt
        return y, m, d, utc_dt, sign, offdelt
    by, bm, bd, _, bsign, boff = parse_to_utc(bl)
    _, _, _, curutc, _, _ = parse_to_utc(cl)
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    sy = curutc.year - 1
    for ty in range(sy, sy + 3):
        ty, tm, td = ty, bm, bd
        if tm == 2 and td == 29 and not is_leap(ty):
            td = 28
        bloc = datetime.datetime(ty, tm, td)
        if bsign == 1:
            butc = bloc - boff
        else:
            butc = bloc + boff
        secdiff = (butc - curutc).total_seconds()
        if secdiff >= 0:
            if secdiff == 0:
                print(0)
            else:
                days = int((secdiff + 86399) // 86400)
                print(days)
            break
solve()