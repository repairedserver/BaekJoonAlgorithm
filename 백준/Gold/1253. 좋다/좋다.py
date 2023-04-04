ans = 0
n = int(input())
num = list(map(int, input().split()))
num.sort()
for i in range(n):
    tmp = num[:i] + num[i+1:]
    left = 0
    right = len(tmp) - 1
    while left < right:
        a = tmp[left] + tmp[right]
        if a == num[i]:
            ans += 1
            break
        if a < num[i]:
            left += 1
        else:
            right -= 1
print(ans)