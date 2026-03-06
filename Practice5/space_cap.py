import re
t = "HelloWorldPython"
r = re.sub(r"([A-Z])", r" \1", t).strip()
print(r)