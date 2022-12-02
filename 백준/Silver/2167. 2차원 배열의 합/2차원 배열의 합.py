n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = l[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for i in range(k):
    a, b, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][b-1] - dp[a-1][y] + dp[a-1][b-1])