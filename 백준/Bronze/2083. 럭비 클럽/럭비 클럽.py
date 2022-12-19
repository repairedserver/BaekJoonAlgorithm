
while True:
    n, a, w = input().split()
    a, w = int(a), int(w)
    if n == '#' and a == 0 and w == 0:
        break

    if a > 17 or w >= 80:
        print("%s Senior" % n)
    else:
        print("%s Junior" % n)