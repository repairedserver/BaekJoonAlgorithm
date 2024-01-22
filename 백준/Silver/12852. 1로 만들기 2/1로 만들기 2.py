n = int(input())
dp = [0] * 1000001
res = [n]
a = n

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
t = dp[n]-1

for i in range(n, 0, -1):
    if (i+1 == a or i*2 == a or i*3 == a) and dp[i] == t:
        t -= 1
        a = i
        res.append(i)

for i in res:
    print(i, end=' ')