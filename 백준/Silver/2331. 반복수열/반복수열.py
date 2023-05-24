n, m = map(int, input().split())
c = n
nums = [c]
while True:
    num = 0
    t = str(c)
    for i in t:
        num += int(i) ** m
    if num in nums:
        nums = nums[:nums.index(num)]
        break
    else:
        nums.append(num)
        c = num
print(len(nums))