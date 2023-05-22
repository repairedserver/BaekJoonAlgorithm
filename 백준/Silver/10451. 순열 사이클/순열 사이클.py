import sys
input = sys.stdin.readline
def dfs(v):
    visited[v] = 1
    next = graph[v]
    if visited[next] == 0: 
        dfs(next)

for i in range(int(input())):
    ans = 0
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
            ans += 1
    print(ans)