import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999)

n = int(input())
graph = [[] for i in range(n + 1)]
visited = [0] * (n + 1)
arr = []

def dfs(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            dfs(i)
            
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for x in range(2, n + 1):
    print(visited[x])