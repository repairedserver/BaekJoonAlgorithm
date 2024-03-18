for i in range(int(input())):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    if len(a) != len(b):
        print("Impossible")
        continue
    for i in range(len(a)):
        if a[i] != b[i]:
            f = False
            break
        else:
            f = True
    if f:
        print("Possible")
    else:
        print("Impossible")