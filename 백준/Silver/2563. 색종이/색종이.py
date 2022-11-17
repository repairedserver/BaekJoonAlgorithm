n = int(input())
p = [[0 for _ in range(101)] for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            p[j][k] = 1

ans = 0
for i in p:
    ans += i.count(1)
print(ans)