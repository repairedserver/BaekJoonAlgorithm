n = int(input())
g = [list(map(int, input())) for i in range(n)]
def yee(x, y, n):
    c = g[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if c != g[i][j]:
                c = -1
                break
    if c == -1:
        print("(", end='')
        n = n // 2
        yee(x, y, n)
        yee(x, y + n, n)
        yee(x + n, y, n)
        yee(x + n, y + n, n)
        print(")", end='')
    elif c == 1:
        print(1, end='')
    else:
        print(0, end='')
yee(0, 0, n)