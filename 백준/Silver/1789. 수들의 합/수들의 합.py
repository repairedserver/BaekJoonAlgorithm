s = int(input())
t = 0
c = 0
while True:
    c += 1
    t += c
    if t > s:
        break
print(c-1)