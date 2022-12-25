while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n+1):
        cnt += i
    print(cnt)
    