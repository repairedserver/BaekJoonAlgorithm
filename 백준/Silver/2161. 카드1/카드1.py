n = int(input())
c = [i for i in range(1, n + 1)]
r = []

while True:
    r.append(c.pop(0))
    if not c:
        break
    c.append(c.pop(0))

print(*r)