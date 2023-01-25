def f(n, cnt):
    if len(n) > 1:
        cnt += 1
        a = 0
        for i in n:
            a += int(i)
        f(str(a), cnt)
    else:
        if int(n) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")


n = input()
cnt = 0
f(n, cnt)