n = int(input())
w = input()
nums = [0] * n
st = []

for i in range(n):
    nums[i] = int(input())

for i in w:					
    if 'A' <= i <= 'Z':
        st.append(nums[ord(i)-ord('A')])
    else :
        s2 = st.pop()
        s1 = st.pop()
        if i == '+':
            st.append(s1 + s2)
        elif i == '-':
            st.append(s1 - s2)
        elif i == '*':
            st.append(s1 * s2)
        elif i == '/':
            st.append(s1 / s2)
print('%.2f' % st[0])