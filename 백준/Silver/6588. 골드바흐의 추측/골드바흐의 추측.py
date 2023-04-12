import sys
input = sys.stdin.readline
arr = [False, False] + [True] * 1000000
for i in range(2, 1001):
    if arr[i] == True:
        for j in range(i + i, 1000001, i):
            arr[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n + 1, 2):
        if arr[i] and arr[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
        i += 2