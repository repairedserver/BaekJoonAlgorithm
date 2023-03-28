n = int(input())
for i in range(n):
    mars = list(map(str, input().split()))
    ans = 0
    for j in range(len(mars)):
        if j == 0:
            ans += float(mars[j])
        else:
            if mars[j] == "#":
                ans -= 7
            elif mars[j] == "%":
                ans += 5
            elif mars[j] == "@":
                ans *= 3
    print("%0.2f" % ans)