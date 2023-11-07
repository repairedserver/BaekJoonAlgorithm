ans = 0
num = 9
d = {}
w = []
n = int(input())

for i in range(n):
    w.append(input())
    
for i in w:
    cnt = len(i)
    for j in i:
        if j not in d:
            d[j] = 10 ** (cnt-1)
        else:
            d[j] += 10 ** (cnt-1)
        cnt -= 1

values = list(d.values())
values.sort(reverse=True)

for i in values:
    ans += i * num
    num -= 1
print(ans)