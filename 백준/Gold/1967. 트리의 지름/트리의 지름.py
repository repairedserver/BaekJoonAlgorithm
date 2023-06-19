import sys
sys.setrecursionlimit(99999)
n = int(input())
tree = [[] for i in range(n+1)]
visited = [-1] * (n+1)
visited[1] = 0
idx = 0
tmp = 0

for i in range(n-1):
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u, w])
    
def dfs(node, cost):
    for i, j in tree[node]:
        cal_w = cost + j
        if visited[i] == -1:
            visited[i] = cal_w
            dfs(i, cal_w)
    return

visited = [-1] * (n+1)
visited[1] = 0

dfs(1, 0) 
for i in range(1, len(visited)):
    if visited[i] > tmp:
        tmp = visited[i]
        idx = i

visited = [-1] * (n+1)
visited[idx] = 0
dfs(idx, 0)
print(max(visited))