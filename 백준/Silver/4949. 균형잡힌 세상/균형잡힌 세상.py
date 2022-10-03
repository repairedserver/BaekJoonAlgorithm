while True:
    n = input()
    if n == '.':
        break
    st = []
    r = 'yes'
    
    for i in n:
        if i == '(' or i == '[':
            st.append(i)
        elif i == ')' :
            if len(st) != 0 and st[-1] == '(':
                st.pop()
            else :
                r = 'no'
                break
        elif i == ']':
            if len(st) != 0 and st[-1] == '[':
                st.pop()
            else :
                r = 'no'
                break
    if len(st) == 0:
        print(r)
    else:
        print('no')