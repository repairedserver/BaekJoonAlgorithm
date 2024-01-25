import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    global d
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and graph[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1
                if d < graph[nz][nx][ny]:
                    d = graph[nz][nx][ny]-1


m, n, h = map(int, input().split())
graph = []
q = deque([])
d = 0

for z in range(h):
    g1 = []
    for x in range(n):
        g1.append(list(map(int, input().split())))
        for y in range(m):
            if g1[x][y] == 1:
                q.append((z, x, y))
    graph.append(g1)
    
bfs()
for x in range(h):
    for y in range(n):
        if 0 in graph[x][y]:
            print(-1)
            exit()
        if x == h-1 and y == n-1:
            print(d)