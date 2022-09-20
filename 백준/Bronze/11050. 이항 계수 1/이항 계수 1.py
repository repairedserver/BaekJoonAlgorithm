from math import factorial
n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))