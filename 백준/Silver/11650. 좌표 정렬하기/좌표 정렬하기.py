n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for i in range(n):
    print(arr[i][0],arr[i][1])