n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in a:
    if i == 1:
        cnt += 1
        ans += cnt
    else:
        cnt = 0
print(ans)