n, m = map(int, input().split())
cnt = 0

arr = [True] * (int(m ** 0.5) + 1)
arr[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if arr[i]:
        if i * i > int(m ** 0.5):
            break
        for j in range(i ** 2, int(m ** 0.5) + 1, i):
            arr[j] = False

for i in range(1, len(arr)):
    if arr[i]:
        res = i * i
        while True:
            if res < n:
                res *= i
                continue
            if res > m:
                break
            res *= i
            cnt += 1

print(cnt)