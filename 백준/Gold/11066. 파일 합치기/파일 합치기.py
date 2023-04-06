import math
import sys
input = sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = [int(x) for x in input().split()]
  dp = [[0 for i in range(n)] for i in range(n)]
  for j in range(1, n):
    for i in range(j - 1, -1, -1):
      s = math.inf
      for k in range(j-i):
        s = min(s, dp[i][i + k] + dp[i + k + 1][j])
      dp[i][j] = s + sum(arr[i:j + 1])
  print(dp[0][n - 1])
