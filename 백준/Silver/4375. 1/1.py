while True:
    try:
        n = int(input())
    except:
        break
    cnt = 1
    num = 1
    while True:
        if num%n != 0:
            num = 10*num + 1
            cnt += 1
        else:
            break
    print(cnt)