n = int(input())
x, y = map(str, input().split("*"))
xl = len(x)
yl = len(y)
for i in range(n):
    a = input()
    if len(a) < xl + yl:
        print("NE")
    elif a[:xl] == x and a[-yl:] == y:
        print("DA")
    else:
        print("NE")