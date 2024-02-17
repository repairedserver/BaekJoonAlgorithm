from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    global cnt
    q = deque([r])
    visited[r] = 1
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for g in graph[v]:
            if visited[g] == 0:
                cnt += 1
                visited[g] = cnt
                q.append(g)
                
n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(r)

for i in visited[1:]:
    print(i)