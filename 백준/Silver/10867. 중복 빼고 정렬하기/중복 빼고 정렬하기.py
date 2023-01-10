n = int(input())
num = list(map(int, input().split()))
num = set(num)
num = sorted(num)
for i in num:
    print(i, end=' ')