n = list(input())
n.sort(reverse=True)
cnt = 0
for i in n:
    cnt += int(i)
if cnt % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))