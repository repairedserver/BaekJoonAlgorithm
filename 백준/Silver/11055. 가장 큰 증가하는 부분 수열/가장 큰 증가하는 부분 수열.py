n = int(input())
a = [int(x) for x in input().split()]
dp = a[:]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])
print(max(dp))