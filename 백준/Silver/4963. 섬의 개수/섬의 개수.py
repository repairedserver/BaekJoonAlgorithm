import sys
sys.setrecursionlimit(99999)
def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    f[x][y] = 0

    for i in range(8):
        x1 = dx[i] + x
        y1 = dy[i] + y
        if 0 <= x1 < m and 0 <= y1 < n and f[x1][y1] == 1:
            dfs(x1, y1)

while True:
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        break
    f = []
    cnt = 0
    for i in range(m):
        f.append(list(map(int, input().split())))
    for i in range(m):
        for j in range(n):
            if f[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)