import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
r = []

for i in range(n):
    st, end = map(int, input().split())
    q.append([st, end])
    
q.sort()
heapq.heappush(r, q[0][1])

for i in range(1, n):
    if r[0] > q[i][0]:
        heapq.heappush(r, q[i][1])
    else:
        heapq.heappop(r)
        heapq.heappush(r, q[i][1])

print(len(r))