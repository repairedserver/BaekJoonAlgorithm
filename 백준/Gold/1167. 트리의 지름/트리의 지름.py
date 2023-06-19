import sys
sys.setrecursionlimit(99999)
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
visited = [-1] * (n+1)
visited[1] = 0
idx = 0
tmp = 0

def dfs(node, cost):
    for i, j in tree[node]:
        cal_w = cost + j
        if visited[i] == -1:
            visited[i] = cal_w
            dfs(i, cal_w)
    return

for i in range(n):
    w = list(map(int, input().split()))
    for j in range(1, len(w)-2, 2):
        tree[w[0]].append([w[j], w[j+1]])

visited = [-1] * (n+1)
visited[1] = 0

dfs(1, 0) 
s = visited.index(max(visited))

visited = [-1] * (n+1)
visited[s] = 0
dfs(s, 0)
print(max(visited))