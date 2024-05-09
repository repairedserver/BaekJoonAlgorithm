n = 1
while True:
    st = []
    cnt = 0
    a = input()
    if '-' in a:
        break
    for j in a:
        if j == '{':
            st.append(j)
        elif j == '}':
            if st:
                st.pop()
            else:
                cnt += 1
                st.append('{')
                
    cnt += len(st)//2
    print(f'{n}. {cnt}')
    n += 1