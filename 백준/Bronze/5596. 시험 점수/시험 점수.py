a1, b1, c1, d1 = map(int, input().split())
a = a1+b1+c1+d1
a2, b2, c2, d2 = map(int, input().split())
b = a2+b2+c2+d2
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(a)