import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    cnt = 0
    for i in range(n):
        t = q.popleft()
        cnt += 1
        if graph[t] == k:
            return cnt
        q.append(graph[t])
    return -1

n, k = map(int, input().split())
graph = [int(input()) for i in range(n)]
print(bfs(0))