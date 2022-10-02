import sys
a = int(sys.stdin.readline())
arr = []
for i in range(a):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
arr.sort(key=lambda x: (x[1], x[0]))

for j in arr:
    print(j[0], j[1])