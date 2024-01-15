n = int(input())
c = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
c.sort(reverse=True)
b.sort(reverse=True)
t = 0
if c[0] < b[0]:
    print(-1)
else:
    while len(b)>0:
        t += 1
        for i in range(n):
            for j in range(len(b)):
                if c[i] >= b[j]:
                    b.pop(j)
                    break
    print(t)