dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
t = int(input())
n = [int(input()) for i in range(t)]
for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009
for i in n:
    print(dp[i])