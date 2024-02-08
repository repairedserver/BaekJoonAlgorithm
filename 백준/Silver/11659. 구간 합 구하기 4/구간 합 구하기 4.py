import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
p = [0]
c = 0

for i in range(n):
    c += num[i]
    p.append(c)

for i in range(m):
    a, b = map(int, input().split())
    print(p[b] - p[a-1])