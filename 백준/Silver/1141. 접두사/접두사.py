ans = 0
n = int(input())
w = [input() for _ in range(n)]
w.sort(key=len)
for i in range(n):
    f = False
    for j in range(i+1, n):
        if w[i] == w[j][0:len(w[i])]:
            f = True
            break
    if not f:
        ans += 1
print(ans)