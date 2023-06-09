import sys
import heapq
input = sys.stdin.readline
maxh = [] 
minh = []

for i in range(int(input())):
    n = int(input())
    if len(maxh) == len(minh):
        heapq.heappush(maxh, -n)
    else:
        heapq.heappush(minh, n)
        
    if len(maxh) >= 1 and len(minh) >= 1 and (maxh[0] * -1) > minh[0]:
        maxv = heapq.heappop(maxh) * -1
        minv = heapq.heappop(minh)
        heapq.heappush(maxh, minv * -1)
        heapq.heappush(minh, maxv)

    print(maxh[0] * -1)