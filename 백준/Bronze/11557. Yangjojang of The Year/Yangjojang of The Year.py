for i in range(int(input())):
    m = 0
    mn = ""
    for i in range(int(input())):
        name, n = input().split()
        n = int(n)
        if n > m:
            m = n
            mn = name
    print(mn)