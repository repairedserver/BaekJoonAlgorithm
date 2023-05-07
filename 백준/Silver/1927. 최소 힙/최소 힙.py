import sys
import heapq
input = sys.stdin.readline
h = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        if len(h):
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, n)