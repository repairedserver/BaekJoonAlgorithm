import sys
sys.setrecursionlimit(999999)
input = sys.stdin.readline

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)
            
n, m, r = map(int, input().split())
graph = [[] for i in range(n+1)]
cnt = 1
visited = [0]*(n+1)

            
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort()

dfs(graph, r, visited)

for i in range(1, n+1):
    print(visited[i])