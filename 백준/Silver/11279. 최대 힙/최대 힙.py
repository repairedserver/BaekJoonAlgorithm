import sys
import heapq as hq
input = sys.stdin.readline
h = []
for i in range(int(input())):
    n = int(input())
    if n == 0:
        try:
            print(-1 * hq.heappop(h))
        except:
            print(0)
    else:
        hq.heappush(h, -n)