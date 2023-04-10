a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split())
ans = ''
while n != 0:
    ans += a[n % b]
    n = n // b
print(ans[::-1])