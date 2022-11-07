n = int(input()) + 1
arr = [0] * n
arr[1] = 1

for i in range(2, n):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n-1])