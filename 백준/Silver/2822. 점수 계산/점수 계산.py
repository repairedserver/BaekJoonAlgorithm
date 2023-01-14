s = []
big = []
tmp = []
su = 0
for i in range(8):
    s.append(int(input()))
ss = sorted(s, reverse=True)

for i in range(5):
    big.append(ss[i])
    
for i in big:
    su += i
    tmp.append(s.index(i))
print(su)

ts = sorted(tmp)
for i in ts:
    print(i + 1, end=' ')