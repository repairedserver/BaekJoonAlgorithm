import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.insert(0, 0)
ans = [0 for i in range(n+1)]
cnt = 1
max_len = -1

for i in range(1, n+1):
    ans[l[i]] = i
    
for i in range(1, n):
    if ans[i+1] > ans[i]:
        cnt += 1
        if cnt > max_len:
            max_len = cnt
    else:
        cnt = 1

if max_len != -1:
    print(n - max_len)
else:
    print(0)