k, n = map(int, input().split())
lan = [int(input()) for i in range(k)]

ans = 0
st, end = 1, max(lan)
while st <= end:
    mid = (st + end) // 2
    temp_sum = 0
    for i in lan:
        temp_sum += i // mid
    if temp_sum >= n:
        st = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)