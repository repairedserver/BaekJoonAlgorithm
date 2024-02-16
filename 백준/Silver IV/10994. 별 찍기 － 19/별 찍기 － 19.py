def star(x, y):
    a = ""
    st = 0
    for i in range(x):
        st = 1 - st
        if st:
            a += "*" 
        else:
            a += " "
    for i in range(y+y-1):
        if x%2 == 0:
            a += "*" 
        else:
            a += " "
    for i in range(x):
        st = 1 - st
        if st:
            a += " " 
        else:
            a += "*"
    a += "\n"
    return a

n = (int(input())*2)-1
ans = ""
for i in range(n, 0, -1): 
    ans += star(n-i,i)
for i in range(2, n+1, 1): 
    ans += star(n-i, i)
print(ans)