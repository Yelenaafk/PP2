import os
import shutil

shutil.copy2("file.txt", "Practice6")
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
os.rmdir("myfolder")