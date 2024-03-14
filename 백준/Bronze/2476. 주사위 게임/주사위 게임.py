ans = 0
for i in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        ans = max(ans, 10000+a*1000)
    elif a == b or a == c:
        ans = max(ans, 1000+a*100)
    elif b == c:
        ans = max(ans, 1000+b*100)
    else:
        ans = max(ans, 100*max(a,b,c))
print(ans)