import sys
input = sys.stdin.readline

n = int(input())
ans = 0
graph = [list(input()) for i in range(n)]
l = [[0] * n for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
                l[i][j] = 1
                
for i in l:
    ans = max(ans, sum(i))
print(ans)