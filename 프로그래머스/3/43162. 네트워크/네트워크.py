def dfs(n, computers, i, v):
    v[i] = True
    for c in range(n):
        if c != i and computers[i][c] == 1:
            if v[c] == False:
                dfs(n, computers, c, v)
                
def solution(n, computers):
    ans = 0
    v = [False for i in range(n)]
    for i in range(n):
        if v[i] == False:
            dfs(n, computers, i, v)
            ans += 1
    return ans