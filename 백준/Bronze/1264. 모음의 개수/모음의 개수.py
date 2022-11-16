while True:
    s = input()
    cnt = 0
    if s == '#':
        break
    for c in s:
        if c in 'aeiouAEIOU':
            cnt += 1
    print(cnt)