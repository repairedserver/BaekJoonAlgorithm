def dfs(x, y):
    a = 1
    q = []
    l[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q.append([x, y])
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<m and l[nx][ny]==1:
                    q.append([nx, ny])
                    l[nx][ny] = 0
                    a += 1
    return a

cnt = 0
ans = 0
n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            ans = max(dfs(i,j), ans)
            cnt += 1

print(cnt)
print(ans)