import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
d = {}

for i in range(n):
    data = input().rstrip()
    d[data] = True

for i in range(m):
    data = input().rstrip()
    if data in d:
        cnt += 1

print(cnt)