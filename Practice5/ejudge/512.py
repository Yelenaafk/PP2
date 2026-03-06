import re
t = input()
s = re.findall(r"\d{2,}", t)
print(" ".join(s))