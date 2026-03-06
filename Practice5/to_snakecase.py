import re
t = "helloWorldPython"
r = re.sub(r"([A-Z])", r"_\1", t).lower()
print(r)