ans = 0
st = []
gwal = input()
for i in range(len(gwal)):
    if gwal[i] == '(':
        st.append(gwal[i])
    else:
        if gwal[i - 1] == '(':
            st.pop()
            ans += len(st)
        else:
            st.pop()
            ans += 1
print(ans)