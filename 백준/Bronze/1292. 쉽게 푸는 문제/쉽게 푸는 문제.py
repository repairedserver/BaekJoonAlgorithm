a, b = map(int, input().split())
t = []
for i in range(1, b + 1):
    for j in range(i):
        t.append(i)
print(sum(t[a-1:b]))