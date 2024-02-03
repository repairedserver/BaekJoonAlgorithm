import sys
input = sys.stdin.readline

n = int(input())
dp = [sys.maxsize] * (n + 1)
dp[0] = 0
a = list(map(int, input().split()))

for i in range(n):
    for j in range(a[i]):
        if i+j+1 < len(dp):
            dp[i+j+1] = min(dp[i]+1, dp[i+j+1])

print(dp[n-1] if dp[n-1] < sys.maxsize else -1)