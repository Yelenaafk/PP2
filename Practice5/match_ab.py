import re
t = "abbb a ab abb"
p = r"ab*"
print(re.findall(p, t))