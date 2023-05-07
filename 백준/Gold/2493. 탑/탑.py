n = int(input())
t = list(map(int, input().split()))
s = []
g = [0] * n
for i in range(n):
    a = t[i]
    while s and t[s[-1]] < a:
        s.pop()
    if s:
        g[i] = s[-1] + 1
    s.append(i)
print(' '.join(list(map(str, g))))