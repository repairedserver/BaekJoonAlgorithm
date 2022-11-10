n = int(input())
ans = 0
for i in range(n):
    inp = input()
    st = []
    for j in inp:
        if len(st) == 0:
                st.append(j)
        else:
            if j == "A":           
                if st[-1] == "B":
                    st.append(j)
                else:
                    st.pop()
            elif j == "B":
                if st[-1] == "A":
                    st.append(j)
                else:
                    st.pop()
    if len(st)==0:
        ans+=1
print(ans)