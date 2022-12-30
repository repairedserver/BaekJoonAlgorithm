import sys
input = sys.stdin.readline
n = int(input())
t = 0
for i in range(n):
    t += int(input())
print(t - (n - 1))