n, m = map(int, input().split())
i = 2
ans = m - n + 1
c = [0] * ans
while i**2 <= m:
    zegop = i**2
    if n % zegop == 0:
        j = n // zegop
    else:
        j = n // zegop + 1
    while zegop*j <= m:
        if not c[zegop * j - n]:
            c[zegop * j - n] = 1
            ans -= 1
        j += 1
    i += 1
print(ans)