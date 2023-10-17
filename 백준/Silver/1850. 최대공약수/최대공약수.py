def gcd(a, b):
    while b > 0:
        a, b = min(a,b), max(a,b)
        a, b = a, b%a
    return a
    
a, b = map(int, input().split())
print("1" * gcd(a, b))