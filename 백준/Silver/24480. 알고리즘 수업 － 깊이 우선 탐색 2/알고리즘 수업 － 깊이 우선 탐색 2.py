import sys
input = sys.stdin.readline
sys.setrecursionlimit(999999)

def dfs(v):
    global cnt
    ans[v] = cnt
    for i in graph[v]:
        if ans[i]:
            continue
        cnt += 1
        dfs(i)
        
n, m, r = map(int,input().split())
graph = [[] for i in range(n+1)]
ans = [0] * (n+1)
cnt = 1

for i in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for l in graph:
    l.sort(reverse=True)

dfs(r)
for i in ans[1:]:
    print(i)