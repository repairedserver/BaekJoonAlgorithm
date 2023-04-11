from itertools import combinations
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    c = combinations(arr, i)
    for j in c:
        if sum(j) == s:
            ans += 1

print(ans)