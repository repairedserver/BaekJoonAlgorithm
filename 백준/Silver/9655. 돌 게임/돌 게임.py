import sys
input = sys.stdin.readline
n = int(input())
d = [-1]*1001
d[1], d[2], d[3] = 1, 0, 1
for i in range(4, n+1):
    if d[i-1] or d[i-3]:
        d[i] = 0
    else:
        d[i] = 1
print('CY' if d[n] == 0 else 'SK')