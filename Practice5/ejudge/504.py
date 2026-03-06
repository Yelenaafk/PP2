import re
t = input()
d = re.findall(r"\d", t)
print(" ".join(d))