while True:
    n = 1
    l = list(map(int, input().split()))
    if l[0] == 0:
        break
    for i in range(l[0]):
        s = l[2 * i + 1]
        m = l[2 * i + 2]
        n = n * s - m
    print(n)