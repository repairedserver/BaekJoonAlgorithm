n = int(input())
res = [n]
for i in range(1, n + 1):
    tmp = [n, i]
    while tmp[-1] >= 0:
        tmp.append(tmp[-2] - tmp[-1])
    tmp.pop()
    if len(tmp) > len(res):
        res = tmp
print(len(res))
print(*res)