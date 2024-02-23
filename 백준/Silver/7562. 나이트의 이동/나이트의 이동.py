import sys
from collections import deque
input = sys.stdin.readline
 
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
 
def bfs(n, a, b, c, d):
    m = [[-1]*n for i in range(n)]
    m[a][b] = 0
    q = deque()
    q.append((a,b))
    while q:
        x,y = q.popleft()
        if x == c and y == d:
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and m[nx][ny] == -1:
                m[nx][ny] = m[x][y]+1
                q.append((nx,ny))
    return m[c][d]
 
for i in range(int(input())):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    ans = bfs(n, a, b, c, d)
    print(ans)