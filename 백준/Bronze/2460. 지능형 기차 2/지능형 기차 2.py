p = 0
mp = 0
for i in range(10):
    out, n = map(int, input().split()) 
    p += n - out
    mp = max(p, mp)     
print(mp)