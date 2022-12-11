a, b = map(int, input().split())
c = list(map(int, input().split()))
for i in c:
    print(i-a*b, end=' ')