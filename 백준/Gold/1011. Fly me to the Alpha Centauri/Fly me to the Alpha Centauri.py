n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    dis = y - x
    mv = 1
    mv1 = 0
    cnt = 0
    while mv1 < dis:
        cnt += 1
        mv1 += mv
        if cnt % 2 == 0:
            mv += 1

    print(cnt)