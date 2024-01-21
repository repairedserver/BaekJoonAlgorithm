def dfs(x, y, cnt):
    global ans
    if cnt == k and x == 0 and y == m-1:
        ans += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]=='.':
                graph[nx][ny] = 'T'
                dfs(nx, ny, cnt+1) 
                graph[nx][ny] = '.'

n, m, k = map(int,input().split())
graph = [list(input()) for i in range(n)]
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph[n-1][0] = 'T'
dfs(n-1, 0, 1)

print(ans)