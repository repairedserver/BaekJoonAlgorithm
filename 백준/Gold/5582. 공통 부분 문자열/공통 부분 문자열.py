ans = 0
s1 = input()
s2 = input()
slen1 = len(s1)
slen2 = len(s2)
dp=[[0] * (slen2 + 1) for i in range(slen1 + 1)]
for i in range(1, slen1 + 1):
    for j in range(1, slen2 + 1):
        if (s1[i-1] == s2[j-1]):
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(dp[i][j], ans)
print(ans)