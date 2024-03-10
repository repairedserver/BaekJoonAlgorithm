def dfs(x, y):
    if g[x][y] == '-':
        g[x][y] = 1
        for i in [1, -1]:
            b = y + i
            if (b > 0 and b < m) and g[x][b] == '-':
                dfs(x, b)
                
    if g[x][y] == '|':
        g[x][y] = 1	
        for i in [1, -1]:
            a = x + i
            if (a > 0 and a < n) and g[a][y] == '|':
                dfs(a, y)

n, m = map(int, input().split())
cnt = 0
g = []
for i in range(n):
    g.append(list(input()))

for i in range(n):
    for j in range(m):
        if g[i][j] == '|' or g[i][j] == '-':
            dfs(i, j)
            cnt += 1

print(cnt)