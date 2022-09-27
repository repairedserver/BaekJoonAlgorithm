import sys
n, k = map(int, sys.stdin.readline().split())

ans = 0
one = 1
nine = 9

while k > nine*one:
    k -= nine*one
    ans += nine

    one += 1
    nine *= 10

ans = (ans+1) + (k-1) // one
if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1) % one])