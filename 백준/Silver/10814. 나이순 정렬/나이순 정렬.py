import sys
input = sys.stdin.readline
a = []
for i in range(int(input())):
    a.append(list(input().split()))
a.sort(key=lambda x: int(x[0]))
for i in range(len(a)):
    print(a[i][0], a[i][1])