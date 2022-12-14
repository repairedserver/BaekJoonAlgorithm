t = []
p = 0
for _ in range(4):
    a, b = map(int, input().split())
    p += b
    p -= a
    t.append(p)

print(max(t))