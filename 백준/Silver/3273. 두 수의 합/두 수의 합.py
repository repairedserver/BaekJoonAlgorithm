n = int(input())
num = list(map(int, input().split()))
num.sort()
a = int(input())
ans = 0
l, r = 0, n - 1
while l < r:
    t = num[l] + num[r]
    if t == a:
        ans += 1
        l += 1
    elif t < a:
        l += 1
    else:
        r -= 1
print(ans)