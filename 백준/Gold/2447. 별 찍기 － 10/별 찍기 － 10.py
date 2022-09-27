def byeol(a):
    if a == 3:
        return ['***', '* *', '***']

    arr = byeol(a//3)
    s = []

    for i in arr:
        s.append(i*3)
    for i in arr:
        s.append(i + ' ' * (a // 3) + i)
    for i in arr:
        s.append(i * 3)

    return s

n = int(input())
print('\n'.join(byeol(n)))