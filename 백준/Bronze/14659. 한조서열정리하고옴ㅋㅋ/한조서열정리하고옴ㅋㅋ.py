n = int(input())
a = list(map(int, input().split()))
ans = []
h = a[0]
cnt = 0
 
for i in range(1, n):
    if h > a[i]:
        cnt += 1
    else:
        h = a[i]
        ans.append(cnt)
        cnt = 0

ans.append(cnt)
print(max(ans))