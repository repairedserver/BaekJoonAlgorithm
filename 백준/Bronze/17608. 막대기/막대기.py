import sys
input = sys.stdin.readline
n = int(input())
l = []
cnt = 0
m = 0
for i in range(n):
	l.append(int(input()))
for i in reversed(l):
	if m < i:
		m = i
		cnt += 1
print(cnt)