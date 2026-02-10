def my_function(*kids): #do not know the number of arguments
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def arguments(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
arguments("Emil", "Tobias", "Linus")

def my_function(**kid): #do not know the number of key=value arguments(details of smth like fname, lname and age)
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")