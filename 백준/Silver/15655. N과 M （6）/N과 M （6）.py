def dfs(st):
    if len(t) == m:
        print(*t)
        return
    for i in range(st, n):
        if num[i] not in t:
            t.append(num[i])
            dfs(i+1)
            t.pop()

n, m = map(int, input().split())
num = list(map(int, input().split()))
t = []
num.sort()
dfs(0)