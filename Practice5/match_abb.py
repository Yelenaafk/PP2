import re
t = "ab abb abbb abbbb"
p = r"ab{2,3}"
print(re.findall(p, t))