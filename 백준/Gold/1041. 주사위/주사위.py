n = int(input())
d = list(map(int, input().split()))
ans = 0
s = (n**2)*5

if n == 1:
    d.sort()
    print(sum(d[:5]))
else:
    b = []
    ans = 0
    for i in range(3):
        b.append(min(d[i], d[-1-i]))
    b.sort()

    ans += sum(b)*4
    s -= 12

    ans += sum(b[:2])*(8*n-12)
    s -= (8*n-12)*2
    
    ans += b[0]*s
    print(ans)