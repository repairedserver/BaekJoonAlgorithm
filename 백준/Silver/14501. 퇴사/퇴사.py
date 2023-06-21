import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
s = [list(map(int, input().split())) for i in range(n)]
for i in range(n-1, -1, -1):
    if n < i+s[i][0]:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], s[i][1] + dp[i + s[i][0]]) 
print(dp[0])