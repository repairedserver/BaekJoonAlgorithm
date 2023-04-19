def func(n, k):
    cnt = 0
    while n > 0:
        n //= k
        cnt += n
    return cnt
n, m = map(int, input().split())
two = func(n, 2) - func(n - m, 2) - func(m, 2)
five = func(n, 5) - func(n - m, 5) - func(m, 5)
print(min(two, five))