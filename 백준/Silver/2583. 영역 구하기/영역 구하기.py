import sys
sys.setrecursionlimit(9999999)

def dfs(x, y):
    global cnt
    if x < 0 or n <= x or y < 0 or m <= y:
        return 0
    if graph[x][y] == 1:
        return 0
    
    graph[x][y] = 1
    cnt += 1
    for i in range(4):
        dfs(x+dx[i], y+dy[i])
    
    return cnt

n, m, k = map(int, input().split())
graph = [[0]*m for i in range(n)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = []

for i in range(n):
    for j in range(m):
        cnt = dfs(i, j)
        if cnt:
            ans.append(cnt)
            cnt = 0          
print(len(ans))
for i in sorted(ans):
    print(i, end=' ')