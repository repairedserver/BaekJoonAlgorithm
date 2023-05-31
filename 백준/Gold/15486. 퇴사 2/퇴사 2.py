import sys
input = sys.stdin.readline
n = int(input())
a = [0] * (n + 1)
b = [0] * (n + 1)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    a[i], b[i] = map(int, input().split())

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    f = a[i] + i - 1
    if f <= n:
        dp[f] = max(dp[f], dp[i - 1] + b[i])
print(max(dp))