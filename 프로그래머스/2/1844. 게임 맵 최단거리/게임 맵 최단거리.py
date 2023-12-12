from collections import deque
def solution(maps):
    q = deque()
    q.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    
    v = [[False] * m for i in range(n)]
    v[0][0] = True
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = y + dx[i]
            ny = x + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                if not v[ny][nx]:
                    q.append((ny, nx))
                    v[ny][nx] = True
                    maps[ny][nx] = maps[x][y] + 1
                    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]