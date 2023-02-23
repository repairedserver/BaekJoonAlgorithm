n, m = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
l, r = 0, 1
while r <= n and l <= r:
    s = num[l:r]
    t = sum(s)

    if t == m:
        cnt += 1

        r += 1

    elif t < m:
        r += 1

    else:
        l += 1
print(cnt)