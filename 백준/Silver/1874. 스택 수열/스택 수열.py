n = int(input())
st = []
ans = []
f = 0
c = 1
for i in range(n):
    num = int(input())
    while c <= num:    
        st.append(c)
        ans.append("+")
        c += 1  

    if st[-1] == num:
        st.pop()
        ans.append("-")
    else:  
        print("NO")
        f = 1
        break               

if f == 0:
    for i in ans:
        print(i)