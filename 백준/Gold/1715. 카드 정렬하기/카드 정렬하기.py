import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
c = []
total = 0

for i in range(n):
    hq.heappush(c, int(input()))

while len(c) > 1:
    a = hq.heappop(c)
    b = hq.heappop(c)
    total += a+b
    hq.heappush(c, a+b)

print(total)