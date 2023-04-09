n = int(input())
a = 2
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(a):
        if j == 0:
            l[i][j] = l[i][j] + l[i - 1][j]
        elif i == j:
            l[i][j] = l[i][j] + l[i - 1][j - 1]
        else:
            l[i][j] = max(l[i - 1][j - 1], l[i - 1][j]) + l[i][j]
    a += 1
print(max(l[n - 1]))