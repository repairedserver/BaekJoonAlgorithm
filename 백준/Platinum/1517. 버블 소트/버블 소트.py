def merge(fir, end):
    global count
    if fir < end:
        mid = (fir + end) // 2
        merge(fir, mid)
        merge(mid + 1, end)

        num1 = fir
        num2 = mid + 1
        tmp = []
        while num1 <= mid and num2 <= end:
            if arr[num1] <= arr[num2]:
                tmp.append(arr[num1])
                num1 += 1

            else:
                tmp.append(arr[num2])
                num2 += 1
                count += (mid - num1 + 1) #swap
        if num1 <= mid:
            tmp = tmp + arr[num1:mid+1]
        if num2 <= end:
            tmp = tmp + arr[num2:end+1]

        for i in range(len(tmp)):
            arr[fir + i] = tmp[i]


count = 0
num = int(input())
arr = list(map(int, input().split()))
merge(0, num-1)
print(count)

# 두 요소 간 순서가 맞으면 가만히 두고
# 순서가 틀리다면 교환

# 동일한 원소가 나올시 동일한 원소도 정렬하기때문에 버블정렬 시간초과남
