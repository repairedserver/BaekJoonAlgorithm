birth = []
for i in range(int(input())):
    n, d, m, y = input().rstrip().split()
    d, m, y = map(int, (d, m, y))
    birth.append((y, m, d, n))
birth.sort()
print(birth[-1][3])
print(birth[0][3])