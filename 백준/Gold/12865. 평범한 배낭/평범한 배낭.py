n, k = map(int, input().split())
bag = [[0,0]]
a = []

for i in range(n + 1):
    a.append([0]*(k + 1))

for i in range(n):
    bag.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = bag[i][0]
        v = bag[i][1]
        if j < w:
            a[i][j] = a[i - 1][j]
        else:
            a[i][j] = max(a[i - 1][j], a[i - 1][j - w] + v)

print(a[n][k])