import sys
input = sys.stdin.readline
n = int(input())
coin = [list(input().rstrip()) for i in range(n)]
def reverse(x):
    return 'T' if x == 'H' else 'H'
ans = n**2
for b in range(1 << n):
    s = 0
    for i in range(n):
        t = 0
        for j in range(n):
            c = coin[j][i]
            if (b & (1 << j)) != 0:
                c = reverse(c)
            if c == 'T':
                t += 1
        s += min(t, n-t)
    if s < ans:
        ans = s
print(ans)