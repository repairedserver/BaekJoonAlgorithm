from collections import deque
n = int(input())
q = deque()
q.appendleft(n)
for i in range(n-1, 0, -1):
    q.appendleft(i)
    for j in range(i):
        a = q.pop()
        q.appendleft(a)
print(*q)