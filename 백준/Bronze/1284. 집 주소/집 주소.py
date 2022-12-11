while True:
    n = input()
    if n == '0':
        break
    r = len(n)+1
    for i in n:
        if i == '0':
            r += 4 
        elif i == '1':
            r += 2
        else:
            r += 3
    print(r)