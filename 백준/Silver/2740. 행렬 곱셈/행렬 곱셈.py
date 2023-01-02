import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for i in range(m):
    b.append(list(map(int, input().split())))
c = [[0 for i in range(k)] for i in range(n)]

for n1 in range(n):
    for k1 in range(k):
        for m1 in range(m):
            c[n1][k1] += a[n1][m1] * b[m1][k1]
for i in c:
    for j in i:
        print(j, end = ' ')
    print()