import sys
input = sys.stdin.readline
n = int(input())
d = {}
for i in range(n):
    m = int(input())
    if m in d:
        d[m] += 1
    else:
        d[m] = 1
d = sorted(d.items(), key=lambda a: (-a[1], a[0]))
print(d[0][0])