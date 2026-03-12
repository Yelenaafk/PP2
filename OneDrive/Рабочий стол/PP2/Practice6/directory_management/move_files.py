import os
#create directories
os.mkdir("test")
os.makedirs("test/inner")
#list files in current directory
print(os.listdir())
#change directory
os.chdir("test")
#print current working directory
print(os.getcwd())
#go back to parent directory
os.chdir("..")
#remove directories
os.rmdir("test/inner")
os.rmdir("test")