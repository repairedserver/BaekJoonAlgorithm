from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
q = deque()
ch = False

for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

dis = [-1] * (n+1)
dis[x] = 0
q.append(x)

while q:
    a = q.popleft()
    for i in graph[a] :
        if dis[i] == -1:
            dis[i] = dis[a] + 1
            q.append(i)

for i in range(1, n+1):
    if dis[i] == k:
        print(i)
        ch = True

if ch == False:
    print(-1)