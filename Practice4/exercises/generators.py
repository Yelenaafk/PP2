#1
def sqrt_gen(n):
    for i in range(n + 1):
        yield i * i
#2
def even_nums(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
#3
def div_thr_fou(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("\nSquares up to n:")
for value in sqrt_gen(n):
    print(value)
    
print("\nEven numbers up to n (comma separated):")
print(",".join(str(num) for num in even_nums(n)))

print("\nNumbers divisible by 3 and 4 up to n:")
for num in div_thr_fou(n):
    print(num)

print("\nSquares from a to b:")
for value in squares(a, b):
    print(value)

print("\nCountdown from n to 0:")
for num in countdown(n):
    print(num)