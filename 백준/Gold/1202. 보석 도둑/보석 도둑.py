import sys
import heapq
input = sys.stdin.readline
ans = 0
tmp = []
n, k = map(int, input().split())
j = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(k)]
j.sort()
b.sort()
for bag in b:
    while j and bag >= j[0][0]:
        heapq.heappush(tmp, -j[0][1])
        heapq.heappop(j)
    if tmp:
        ans += heapq.heappop(tmp)
    elif not j:
        break
print(-ans)