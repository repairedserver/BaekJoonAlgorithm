from collections import deque

def bfs() :
    visited = [[False]*m for i in range(n)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if not visited[nx][ny]:
                if a[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                elif a[nx][ny] == 1:
                    a[nx][ny] = 0
                    visited[nx][ny] = True
                    cnt += 1

    cheese.append(cnt)
    return cnt

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
t = 0
cheese = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True :
    cnt = bfs()
    if cnt == 0 :
        break
    t += 1

print(t)
print(cheese[-2])