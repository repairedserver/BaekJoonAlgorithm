a = [0 for i in range(101)]
a[1] = a[2] = a[3] = 1
for i in range(98):
    a[i + 3] = a[i] + a[i + 1]
for i in range(int(input())):
    n = int(input())
    print(a[n])