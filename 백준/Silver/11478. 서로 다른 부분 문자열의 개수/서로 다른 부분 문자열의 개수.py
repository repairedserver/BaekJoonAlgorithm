a = input()
s = set()
for i in range(len(a)):
    for j in range(i, len(a)):
        s.add(a[i:j+1])
print(len(s))