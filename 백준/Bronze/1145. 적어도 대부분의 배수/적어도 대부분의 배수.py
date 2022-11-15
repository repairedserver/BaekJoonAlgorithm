arr = list(map(int, input().split()))
m = min(arr)
cnt = 0
while True:
    cnt = 0
    for i in range(len(arr)):
        if m % arr[i] == 0 :
            cnt += 1
    if cnt >= 3:
        print(m)
        break
    m += 1