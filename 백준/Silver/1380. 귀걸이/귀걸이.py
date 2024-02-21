def ear(n):
    name = [input() for i in range(n)]
    ring = {}
    for i in range(n*2-1):
        a, b = list(map(str, input().split()))
        ring[a] = ring.get(a, 0)+1
        
    for k, v in ring.items():
        if v == 1:
            return name[int(k)-1]

cnt = 1
ans = []
while True:
    n = int(input())
    if n == 0: 
        break
    print(cnt, ear(n))
    cnt += 1