n = int(input().rstrip())

bo = [list(map(int,input().split())) for i in range(n)]
ze = 0
one = 0
min_one=0
def sol(y,x,n):
    global ze, one, min_one
    ini = bo[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if bo[i][j] != ini:
                for k in range(3):
                    for l in range(3):
                        sol(y+k*n//3,x+l*n//3,n//3)
                return
    if ini==0:
        ze+=1
    elif ini==1:
        one+=1
    elif ini==-1:
        min_one+=1
    return

sol(0,0,n)

print(min_one)
print(ze)
print(one)