n, m = map(int, input().split())
dna = []
for i in range(n):
    dna.append(input())
cnt = 0
res = ''
for i in range(m):
    c = [0, 0, 0, 0]
    for j in range(n):
        if dna[j][i] == 'A':
            c[0] += 1
        elif dna[j][i] == 'C':
            c[1] += 1
        elif dna[j][i] == 'G':
             c[2] += 1
        elif dna[j][i] == 'T':
            c[3] += 1
    idx = c.index(max(c))
    if idx == 0:
        res += 'A'
    elif idx == 1:
        res += 'C'
    elif idx == 2:
         res += 'G'
    elif idx == 3:
        res += 'T'
    cnt += n - max(c)

print(res)
print(cnt)