def solution(s):
    st = []
    for i in s:
        if i == '(':
            st.append(i)
        else:
            if st == []:
                return False
            else:
                st.pop()
    if st == []:
        return True
    else:
        return False