from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
    q.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    v[x][y] = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == a[x][y] and not v[nx][ny]:
                v[nx][ny] = 1
                q.append((nx,ny))

q = deque()
n = int(input())
a = [list(input()) for i in range(n)]

v = [[0]*n for i in range(n)]
c1 = 0
c2 = 0
for i in range(n):
    for j in range(n):
        if not v[i][j]:
            BFS(i, j)
            c1 += 1

for i in range(n):
    for j in range(n):
        if a[i][j] == 'G':
            a[i][j] = 'R'

v = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if not v[i][j]:
            BFS(i,j)
            c2 += 1

print(c1, c2)