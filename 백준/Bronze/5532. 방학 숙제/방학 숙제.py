l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a//c > b//d:
    if a%c == 0:
        print(l-a//c)
    else:
        print(l-1-a//c)
else:
    if b%d == 0:
        print(l-b//d)
    else:
        print(l-1-b//d)