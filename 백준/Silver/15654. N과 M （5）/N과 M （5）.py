def dfs():
    if len(temp) == m:
        print(*temp)
        return
    for i in range(n):
        if num[i] not in temp:
            temp.append(num[i])
            dfs()
            temp.pop()
n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
temp = []
dfs()