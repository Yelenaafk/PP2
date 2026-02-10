def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def helloname(name): # name is a parameter
  print("Hello", name)
helloname("Emil") # "Emil" is an argument

def FNLN(fname, lname):
  print(fname + " " + lname)
FNLN("Emil", "Refsnes")

def friend(name = "friend"):
  print("Hello", name)
friend("Emil")
friend("Tobias")
friend()
friend("Linus")