import math
n = int(input())
for i in range(n):
    x1, y1, z1, x2, y2, z2 = list(map(int, input().split()))
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d == 0:
        if z1 == z2:
            print(-1)
        else:
            print(0)
    else:
        if z1 + z2 == d or abs(z2 - z1) == d:
            print(1)
        elif abs(z1 - z2) < d and d < abs(z1 + z2):
            print(2)
        else:
            print(0)