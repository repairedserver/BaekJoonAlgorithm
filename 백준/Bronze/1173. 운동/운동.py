N, m, M, T, R = map(int, input().split())
x = m
t = N
cnt = 0
if m + T > M:
    print(-1)
else:
    while N > 0:
        if x + T <= M:
            x += T
            N -= 1
        else:
            if x - R >= m:
                x -= R
            else:
                x = m
            t += 1
    print(t)