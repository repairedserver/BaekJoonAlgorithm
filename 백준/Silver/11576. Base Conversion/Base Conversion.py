import math 
a, b = map(int, input().split())
n = int(input())
l = list(map(int, input().split()))
ten = 0
res = []
for i in range(n):
    ten += int(l[i] * math.pow(a, n - i - 1))
while ten:
    nam = ten % b
    res.append(str(nam))
    ten = ten // b
res = res[::-1]
print(' '.join(res))