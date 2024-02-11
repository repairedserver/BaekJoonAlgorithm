a, b = map(int, input().split())
c = (b*100) // a
ans = 0
l = 1
r = a
if c >= 99:
    print(-1)
else:
    while l <= r:
        m = (l+r) // 2
        if (b+m)*100 // (a+m) <= c:
            l = m+1
        else:
            ans = m
            r = m-1
    print(ans)