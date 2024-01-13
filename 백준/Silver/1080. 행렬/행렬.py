def trans(i, j, l1):
    for x in range(i, i+3):
        for y in range(j, j+3):
            l1[x][y] = 1-l1[x][y]
            
n, m = map(int, input().split())
cnt = 0
l1 = [list(map(int, list(input()))) for i in range(n)]
l2 = [list(map(int, list(input()))) for i in range(n)]

for i in range(n-2):
    for j in range(m-2):
        if l1[i][j] != l2[i][j]:
            cnt += 1
            trans(i, j, l1)

if l1 != l2:
    print(-1)
else:
    print(cnt)