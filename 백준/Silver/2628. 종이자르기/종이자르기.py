w,h = map(int, input().split())
n = int(input())
ans = 0
wi = [0, w]
he = [0, h]
for i in range(n):
    a, b = map(int, input().split())
    if a == 1:
        wi.append(b)
    elif a == 0:
        he.append(b)
wi.sort()
he.sort()
for i in range(len(wi) - 1):
    for j in range(len(he) - 1):
        x = wi[i + 1] - wi[i]
        y = he[j + 1] - he[j]
        ans = max(ans, x * y)
print(ans)