n = int(input())
t = []
l = 0
cnt = 0
for i in range(n):
    st, end = map(int, input().split())
    t.append([st, end])
t = sorted(t, key=lambda a: a[0])
t = sorted(t, key=lambda a: a[1])
for i, j in t:
    if i >= l:
        cnt += 1
        l = j
print(cnt)