n = int(input())
m = list(map(int, input().split()))
for i in range(1, n):
    m[i] = max(m[i], m[i-1] + m[i])
    
print(max(m))
