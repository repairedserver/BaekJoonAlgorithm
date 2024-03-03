import sys
sys.setrecursionlimit(999999)
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    visited[x][y] = True
    if graph[x][y] == 'P':
        cnt += 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] != "X":
                dfs(nx,ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
n, m = map(int,input().split())
visited = [[False] * m for i in range(n)]
graph = list(input() for i in range(n))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            dfs(i, j)
if cnt == 0:
    print("TT")
else:
    print(cnt)