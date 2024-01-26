from collections import deque
import sys 
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort()

def bfs(graph, st, visited):
    q = deque([st])
    visited[st] = 1
    cnt = 2

    while q :
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = cnt
                cnt += 1

bfs(graph, r, visited)

for i in visited[1:]:
    print(i)