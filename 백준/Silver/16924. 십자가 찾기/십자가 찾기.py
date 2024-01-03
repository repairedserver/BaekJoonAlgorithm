import sys
input = sys.stdin.readline

def check(i, j, s, v):
    cnt = 0
    ans = []
    
    for k in range(1, s+1):
        if b[i-k][j] == '*' and b[i+k][j] == '*' and b[i][j-k] == '*' and b[i][j+k] == '*':
            cnt = 1
            ans = [i+1, j+1, k]
            v[i][j] = 0
            v[i-k][j] = 0
            v[i+k][j] = 0
            v[i][j-k] = 0
            v[i][j+k] = 0
        else:
            return 1, ans
        
    return cnt, ans

n, m = map(int, input().split())
v = [[0 for i in range(m)] for i in range(n)]
cnt = 0
hap = 0
ans = []
b = []

for i in range(n):
    b.append(list(sys.stdin.readline()))

for i in range(n):
    for j in range(m):
        if b[i][j] == '*':
            v[i][j] = 1

for i in range(1, n-1):
    for j in range(1, m-1):
        if b[i][j] == '*':
            s = min(i, n-i-1, j, m-j-1)
            ac, aa = check(i, j, s, v)
            if aa:
                ans.append(aa)
                cnt += ac

for i in v:
    hap += sum(i)

if hap == 0:
    print(cnt)
    for i in ans:
        print(i[0], i[1], i[2])
else:
    print(-1)