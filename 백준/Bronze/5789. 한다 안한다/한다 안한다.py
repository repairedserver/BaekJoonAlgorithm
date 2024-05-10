for i in range(int(input())):
    a = input()
    b = len(a)
    if a[b//2-1] == a[b//2]:
        print('Do-it')
    else:
        print('Do-it-Not')