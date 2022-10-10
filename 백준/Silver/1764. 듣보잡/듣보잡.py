n, m = map(int,input().split())
arr1 = set()
arr2 = set()

for i in range(n):
    arr1.add(input())
for i in range(m):
    arr2.add(input())

arr = sorted(list(arr1 & arr2))
print(len(arr))

for i in arr:
    print(i)