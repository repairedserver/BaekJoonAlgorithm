n = int(input())
p = []

for _ in range(n):
    x, y = map(int, input().split())
    p.append((x,y))

for i in p:
    r = 1
    for j in p:
        if i[0] < j[0] and i[1] < j[1]:
            r+=1
    print(r, end = " ")