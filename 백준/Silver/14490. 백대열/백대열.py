def g(n, m):
    if m == 0:
        return n
    return g(m, n % m)
n, m = map(int, input().split(':'))
a = g(max(n, m), min(n, m))
print(f"{n//a}:{m//a}")