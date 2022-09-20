t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:
        num = n//h
        floor = h
    print(floor*100+num)