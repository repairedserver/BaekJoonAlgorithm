def solution(m, n, puddles):
    pud = [[q,p] for [p,q] in puddles]
    dp = [[0]*(m+1) for i in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [i, j] in pud:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000007  

    return dp[n][m]