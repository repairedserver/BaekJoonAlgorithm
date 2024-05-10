for i in range(int(input())):
    a = input()
    b = a[:len(a)//2]
    c = (a[len(a)//2:])[::-1]
    for i in range(len(b)):
        if b[i] == c[i]:
            ans = 'Do-it'
        else:
            ans = 'Do-it-Not'
    print(ans)