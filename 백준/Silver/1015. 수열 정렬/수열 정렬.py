import sys
input = sys.stdin.readline
n = int(input())
ans = [0] * n
a = list(map(int, input().split()))
sa = sorted(a)
for i in range(n):
    idx = sa.index(a[i])
    ans[i] = idx
    sa[idx] = -1
print(*ans)