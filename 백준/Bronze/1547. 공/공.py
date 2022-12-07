n = int(input())
c = [1,2,3]
for i in range(n):
    x, y = map(int, input().split())
    a = c.index(x)
    b = c.index(y)
    c[a], c[b] = c[b], c[a]
print(c[0])