n, m = map(int, input().split())
a = int(input())

cnt = 0
l = 1
r = m
 
for i in range(a):
    p = int(input())
 
    if l <= p and r >= p:
        continue
    elif l > p:
        cnt += l-p
        r -= l-p
        l = p
    else:
        cnt += p-r
        l += p-r
        r = p
        
print(cnt)