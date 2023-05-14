import sys
input = sys.stdin.readline
n = int(input())
w = []
d = [0] * n
for i in range(n):
    w.append(int(input()))
d[0] = w[0]
if n > 1:
    d[1] = w[0] + w[1]
if n > 2:
    d[2] = max(w[2] + w[1], w[2] + w[0], d[1])
for i in range(3, n):
    d[i] = max(d[i-1], d[i-3] + w[i-1] + w[i], d[i-2] + w[i])
print(d[n-1])