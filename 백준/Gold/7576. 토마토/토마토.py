from collections import deque
m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
q = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:
            q.append([i, j])

def yee():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
                mat[nx][ny] = mat[x][y] + 1
                q.append([nx, ny])

yee()
for i in mat:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    res = max(res, max(i))
print(res - 1)