import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

for i in range(1, n + 1):
    if visited[i] == False:
        cnt += 1
        dfs(i)

print(cnt)