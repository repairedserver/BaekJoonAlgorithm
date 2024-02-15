m = int(input())
st = [[' ' for _ in range(m*2)] for i in range(m)]

def star(x, y, n):
    if n <= 3:
        for i in range(3):
            for j in range(i+1):
                st[x+i][y+j] = st[x+i][y-j] = '*'
        st[x+1][y] = ' '
        return None
    
    m = n // 2
    star(x, y, m)
    star(x+m, y-m, m)
    star(x+m, y+m, m)

star(0, m-1, m)

for i in range(m):
    print("".join(st[i]))