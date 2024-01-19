from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        t = q.popleft()
        for i in graph[t]:
            if not visited[i]:
                visited[i] = visited[t]+1
                q.append(i)


n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
ans = []

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    ans.append(sum(visited))

print(ans.index(min(ans))+1)