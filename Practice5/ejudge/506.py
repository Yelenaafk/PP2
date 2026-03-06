import re
t = input()
m = re.search(r"\S+@\S+\.\S+", t)
if m:
    print(m.group())
else:
    print("No email")