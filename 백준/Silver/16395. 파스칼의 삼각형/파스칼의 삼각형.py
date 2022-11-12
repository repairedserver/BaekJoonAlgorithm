n, k = map(int, input().split())
arr = [[1], [1, 1]]
for i in range(2, n):
    row = [1]
    for j in range(1, i):
        row.append(arr[i-1][j-1]+arr[i-1][j])
    row.append(1)
    arr.append(row)
print(arr[n-1][k-1])