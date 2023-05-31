n = int(input())
m = int(input())
v = []
sit = [1, 1, 2]
ans = 1
p = 0

for i in range(m):
    k = int(input())
    v.append(k)
    
for i in range(3, 41):
    sit.append(sit[i - 2] + sit[i - 1])

if m >= 1:
    for i in range(m):
        ans *= sit[v[i] - 1 - p]
        p = v[i]
    ans *= sit[n - p]
else:
    ans = sit[n]
print(ans)