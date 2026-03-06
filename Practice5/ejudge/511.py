import re
t = input()
n = re.findall(r"[A-Z]", t)
print(len(n))