def dfs(n):
    for i in cow[n]:
        if c[i]:
            continue
        c[i] = True
        if visit[i] == -1 or dfs(visit[i]):
            visit[i] = n
            return True
    return False
n, m = map(int, input().split())
cow = [[] for i in range(n)]
visit = [-1] * m
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    for j in a[1:]:
        j -= 1
        cow[i].append(j)
for i in range(n):
    c = [False] * m
    if dfs(i):
        ans += 1
print(ans)