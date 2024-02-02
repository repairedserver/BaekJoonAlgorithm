import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def bfs(graph):
    q = deque([(j, i) for i in range(n) for j in range(m) if graph[i][j] == 2])
    while q:
        x, y = q.popleft()
        for nx, ny in zip([x+1, x-1, x, x], [y, y, y+1, y-1]):
            if 0 <= nx < m and 0 <= ny < n and not graph[ny][nx]:
                graph[ny][nx] = 2
                q.append((nx, ny))
    
    global ans
    cnt = sum([i.count(0) for i in graph])
    ans = max(ans, cnt)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
xy = [(x, y) for x in range(m) for y in range(n) if not graph[y][x]]
ans = 0

for c in combinations(xy, 3):
    t_graph = deepcopy(graph)
    for x, y in c:
        t_graph[y][x] = 1
    bfs(t_graph)

print(ans)