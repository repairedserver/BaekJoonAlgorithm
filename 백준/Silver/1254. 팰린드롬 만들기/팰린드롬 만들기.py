a = input()
for i in range(len(a)):
    if a[i:] == a[i:][::-1]:
        print(len(a)+i)
        break