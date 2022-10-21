import sys
sys.setrecursionlimit(10000)
def d(x, y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if g[ny][nx] == 1:
                g[ny][nx] = -1
                d(nx, ny)
t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    g = [[0]*m for i in range(n)]
    cnt = 0
    for j in range(k):
        X, Y = map(int, input().split())
        g[Y][X] = 1
    for x in range(m):
        for y in range(n):
            if g[y][x] == 1:
                d(x, y)
                cnt += 1
    print(cnt)