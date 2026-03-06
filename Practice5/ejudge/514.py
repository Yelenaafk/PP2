import re
t = input()
p = re.compile(r"^\d+$")
if p.fullmatch(t):
    print("Match")
else:
    print("No match")