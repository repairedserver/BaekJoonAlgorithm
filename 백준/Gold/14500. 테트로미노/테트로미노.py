def dfs(i, j, idx, t):
    global ans
    if idx == 3:
        if t > ans:
            ans = t
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if visit[ni][nj] == 0:
                    visit[ni][nj] = 1
                    dfs(ni, nj, idx + 1, t + arr[ni][nj])
                    visit[ni][nj] = 0

def block(i, j, t):
    global ans
    b = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m:
            b += 1
            t += arr[ni][nj]
    if b == 3:
        if t > ans:
            ans = t
    if b == 4:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            t -= arr[ni][nj]
            if t > ans:
                ans = t
            t += arr[ni][nj]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [([0] * m) for i in range(n)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
ans = 0

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        block(i, j, arr[i][j])
        visit[i][j] = 0

print(ans)