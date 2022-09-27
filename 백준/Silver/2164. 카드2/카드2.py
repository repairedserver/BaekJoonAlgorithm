from collections import deque as dq

n = int(input())
dq = dq([i for i in range(1, n+1)])

while (len(dq)>1):
    dq.popleft()
    move = dq.popleft()
    dq.append(move)
print(dq[0])