a = []
s = 0
for i in range(10):
    a.append(int(input()))
for i in a:
    s += i
    if s >= 100:
        if s - 100 > 100 - (s - i):
            s -= i
        break
print(s)