n = int(input())
c =[list(map(int, input().split())) for i in range(n)]

for i in range(1, n):
    c[i][0] += min(c[i-1][1], c[i-1][2])
    c[i][1] += min(c[i-1][0], c[i-1][2])
    c[i][2] += min(c[i-1][0], c[i-1][1])
    
print(min(c[-1]))