import sys
input = sys.stdin.readline

n = int(input())
s = [0 for i in range(301)]
y = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())

y[0] = s[0]
y[1] = s[0] + s[1]
y[2] = max(s[0]+s[2], s[1]+s[2])

for i in range(3, n):
    y[i] = max(y[i-3] + s[i-1] + s[i], y[i-2] + s[i])

print(y[n-1])