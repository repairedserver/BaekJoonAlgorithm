n = int(input()) 
p = list(map(int, input().split()))

p.sort()
ans = 0

for i in range(1, n+1):
    ans += sum(p[0:i])
print(ans)