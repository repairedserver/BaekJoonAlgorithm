for i in range(int(input())):
    a, b, c = map(float, input().split())
    print('$', end='')
    print("{:.2f}".format(a*b*c))
