import re
t = "Hello, world. Python is fun"
r = re.sub(r"[ ,.]", ":", t)
print(r)