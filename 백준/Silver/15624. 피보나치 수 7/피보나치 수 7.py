a = 0
b = 1
for i in range(int(input())):
    a = (a + b) % 1000000007
    b = a % 1000000007
print(a)