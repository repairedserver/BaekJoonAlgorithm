from collections import deque
n, m = map(int, input().split())

peo = deque()
for i in range(1, n+1): peo.append(i)
ans = []

while peo:
    for _ in range(m-1):
        peo.append(peo.popleft())
    ans.append(peo.popleft())

print(str(ans).replace('[', '<').replace(']', '>'))