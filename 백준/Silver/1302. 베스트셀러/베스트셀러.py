n = int(input())
book = {}
for i in range(n):
    a = input()
    if a not in book:
        book[a] = 1
    else:
        book[a] += 1
        
arr = []
n1 = max(book.values())

for i in book:
    if n1 == book[i]:
        arr.append(i)

arr.sort()
print(arr[0])
        
