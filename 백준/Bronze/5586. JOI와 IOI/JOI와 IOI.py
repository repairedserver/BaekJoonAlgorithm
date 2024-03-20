import sys
input = sys.stdin.readline
st = input()
joi = 0
ioi = 0
for i in range(len(st)-2):
    if st[i:i+3] == 'IOI':
        ioi += 1
    if st[i:i+3] == 'JOI':
        joi += 1
print(joi)
print(ioi)