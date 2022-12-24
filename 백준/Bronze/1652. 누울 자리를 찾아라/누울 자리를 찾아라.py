n = int(input())
m = [list(map(str, input().strip())) for i in range(n)]
r = 0
c = 0
for y in range(n):
    cnt = 0
    for x in range(n):
        if m[y][x] == '.':
            cnt += 1
        elif m[y][x] == 'X':
            if cnt >= 2:
                r += 1
            cnt = 0
    if cnt >= 2:
        r += 1
    cnt = 0
for x in range(n):
    cnt = 0
    for y in range(n):
        if m[y][x] == '.':
            cnt += 1
        elif m[y][x] == 'X':
            if cnt >= 2:
                c += 1
            cnt = 0
    if cnt >= 2:
        c += 1
    cnt = 0
print(r, c)