import re
t = input()
n = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", t)
print(len(n))