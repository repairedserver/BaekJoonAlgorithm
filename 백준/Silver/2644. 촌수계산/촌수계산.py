def dfs(v, num):
    num += 1
    visited[v] = True

    if v == b:
        ans.append(num)

    for i in graph[v]:
        if visited[i] == False:
            dfs(i, num)

n = int(input())
a, b = map(int, input().split())
m = int(input())
ans = []
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)

if len(ans) == 0:
    print(-1)
else:
    print(ans[0] - 1)