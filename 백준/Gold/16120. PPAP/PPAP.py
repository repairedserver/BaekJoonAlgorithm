w = input()
if w == 'P' or w == 'PPAP':
    print('PPAP')
else:
    p = ['P','P','A','P']
    st = []
    for i in w:
        st.append(i)
        if st[-4:] == p:
            st.pop()
            st.pop()
            st.pop()
    print('PPAP') if st == p or st == ['P'] else print('NP')