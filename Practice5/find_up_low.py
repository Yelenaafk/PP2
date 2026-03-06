import re
t = "Hello world Test Python"
p = r"[A-Z][a-z]+"
print(re.findall(p, t))