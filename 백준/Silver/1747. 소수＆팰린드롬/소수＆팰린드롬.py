import math

n = int(input())
mv = 0

def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

for i in range(n, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if isPrime(i):
            mv = i
            break

if mv == 0:
    mv = 1003001
print(mv)