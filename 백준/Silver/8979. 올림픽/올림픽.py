n, m = map(int, input().split())
cnt = 1
table = []
for i in range(n):
    rank = list(map(int, input().split()))
    if rank[0] != m:
        table.append(rank)
    else:
        s = rank
for i in range(len(table)):
    if table[i][1] > s[1]:
        cnt += 1
    elif table[i][1] == s[1]:
        if table[i][2] > s[2]:
            cnt += 1
        elif table[i][2] == s[2]:
            if table[i][3] > s[3]:
                cnt += 1
print(cnt)