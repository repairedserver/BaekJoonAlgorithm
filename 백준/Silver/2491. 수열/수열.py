n = int(input())
num = list(map(int,input().split()))
d = [[1] * n for _ in range(2)]

for i in range(1, n):
    if num[i - 1] <= num[i]:
        d[0][i] = d[0][i - 1] + 1                         
    if num[i - 1] >= num[i]:
        d[1][i] = d[1][i - 1] + 1
print(max(map(max, d)))