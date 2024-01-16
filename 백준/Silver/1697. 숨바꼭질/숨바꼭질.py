from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        p = q.popleft()
        if p == m:
            return visited[p]
        for i in (p-1, p+1, 2*p):
            if  0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[p] + 1
                q.append(i)

n, m = map(int, input().split())
visited = [0]*100001
print(bfs(n))