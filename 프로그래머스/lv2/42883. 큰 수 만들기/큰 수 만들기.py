def solution(number, k):
    st = []
    for i in number:
        while k > 0 and st and st[-1] < i:
            st.pop()
            k -= 1
        st.append(i)
    return ''.join(st[:len(st)-k])