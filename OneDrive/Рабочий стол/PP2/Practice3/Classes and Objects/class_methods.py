class Person:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()

class Calculator:
  def add(self, a, b):
    return a + b
  def multiply(self, a, b):
    return a * b
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} ({self.age})"
p1 = Dog("Tobik", 7)
print(p1)

class Cat:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print("Meow!")
p1 = Cat("Snezhok")
del Cat.greet
p1.greet() # This will cause an error