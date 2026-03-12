import os
from pathlib import Path
#create directories safely
Path("test/inner").mkdir(parents=True, exist_ok=True)
#Path object manipulation
file_path = Path("data") / "user_logs" / "test.txt"
print(f"Full Path: {file_path}")
print(f"Filename:  {file_path.name}")
print(f"Extension: {file_path.suffix}")
print(f"Stem:      {file_path.stem}")
#checking existence
path = Path("test") 
if path.exists():
    if path.is_file():
        print("It's a file!")
    elif path.is_dir():
        print("It's a directory!")