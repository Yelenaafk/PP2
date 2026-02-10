from math import isqrt
nums = list(map(int, input().split()))
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, isqrt(n)+1))
primes = list(filter(is_prime, nums))
if primes:
    print(*primes)
else:
    print("No primes")