import re
t = input()
def dd(match):
    return match.group() * 2
r = re.sub(r"\d", dd, t)
print(r)