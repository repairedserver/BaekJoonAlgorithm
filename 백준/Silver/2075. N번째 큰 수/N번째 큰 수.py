n = int(input())
arr = []
for i in range(n):
    arr += list(map(int, input().split()))
    arr = sorted(arr, reverse=True)[:n]
print(arr[-1])