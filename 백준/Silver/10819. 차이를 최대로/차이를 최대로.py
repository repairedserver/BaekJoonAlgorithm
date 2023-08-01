n = int(input())
l = list(map(int ,input().split()))
visited = [False] * n
ans = 0
def re(a):
    global ans
    if len(a) == n:
        t = 0
        for i in range(n-1):
            t += abs(a[i]-a[i+1])
        ans = max(ans, t)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            a.append(l[i])
            re(a)
            visited[i] = False
            a.pop()

re([])
print(ans)