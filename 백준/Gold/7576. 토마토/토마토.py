from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                a[nx][ny] = a[x][y] + 1
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append([i, j])

bfs()
for i in a:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans - 1)