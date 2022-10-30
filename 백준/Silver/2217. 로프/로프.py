n = int(input())
m = []
res = []
for i in range(n):
    m.append(int(input()))
m.sort(reverse=True)
for j in range(n):
    res.append(m[j]*(j+1))
    
print(max(res))