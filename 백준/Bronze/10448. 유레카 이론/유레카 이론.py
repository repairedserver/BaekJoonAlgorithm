num = [i*(i+1)//2 for i in range(1, 46)]
a = [0] * 1001

for i in num:
    for j in num:
        for k in num:
            n = i + j + k
            if n <= 1000:
                a[n] = 1

for i in range(int(input())):
    print(a[int(input())])