n = input()
arr = []
for i in range(len(n)):
    arr.append(n[i:])

arr.sort()
for i in arr:
    print(i)