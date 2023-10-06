def ncm(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans
n, m = map(int, input().split())
print(ncm(n)//(ncm(n-m)*ncm(m)))