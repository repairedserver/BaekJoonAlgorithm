n = int(input())
c = 0
while n != 0:
    n //= 5
    c += n
print(c)