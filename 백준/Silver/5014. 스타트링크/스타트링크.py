import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == g:
            return cnt[g]
        for i in (v+u, v-d):
            if 0 < i <= f and not visited[i]:
                visited[i] = 1
                cnt[i] = cnt[v]+1
                q.append(i)
                
    if cnt[g] == 0:
        return "use the stairs"

f, s, g, u, d = map(int, input().split())
visited = [0 for i in range(f+1)]
cnt = [0 for i in range(f+1)]
print(bfs(s))