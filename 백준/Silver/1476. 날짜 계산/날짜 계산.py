e, s, m = map(int, input().split())
y = 1
while True :
    if (y-e)%15 == 0 and (y-s)%28 == 0 and (y-m)%19 == 0:
        print(y)
        break
    y += 1