import re
t = "HelloWorldPython"
r = re.split(r"(?=[A-Z])", t)
print(r)