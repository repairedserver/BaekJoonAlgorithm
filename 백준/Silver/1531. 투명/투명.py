n, m = map(int, input().split())
l = [[0]*100 for _ in range(100)]
cnt = 0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2+1):
        for k in range(y1, y2+1):
            l[j-1][k-1] += 1
for i in range(100):
    for j in range(100):
        if l[i][j] > m:
            cnt += 1
print(cnt)