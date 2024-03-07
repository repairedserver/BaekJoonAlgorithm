n, k = map(int, input().split())
p = list(input())
ans = 0
for i in range(n):
    if p[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if p[j] == 'H':
                p[j] = 0
                ans += 1
                break
print(ans)