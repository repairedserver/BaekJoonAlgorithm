a = [0, 1, 2]
for i in range(3, 1001):
    a.append(a[i-2] + a[i-1])
n = int(input())
print(a[n] % 10007)