p = int(input())
m = int(input())
s = input()
ans, cnt, i = 0, 0, 0
while i < m-1:
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == p:
            ans += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(ans)