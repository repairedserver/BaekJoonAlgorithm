def dfs(d):
    if d == m:
        print(*l)
        return
    for i in range(n):
        if d == 0 or l[-1] <= num[i]:
            l.append(num[i])
            dfs(d+1)
            l.pop()
        
n, m = map(int, input().split())
num = sorted(map(int, input().split()))
l = []
dfs(0)