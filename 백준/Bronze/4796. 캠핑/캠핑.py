cnt = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    i = v // p
    j = v % p
    if l < j:
        j = l
    print(f'Case {cnt}: {i*l+j}')
    cnt += 1