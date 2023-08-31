a, b = map(int, input().split())
n = int(input())
if a+b >= n*2:
    print((a+b)-n*2)
else:
    print(a+b)