import sys
n, m = map(int, input().split())

pint = {}
pname = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    pint[i] = name
    pname[name] = i

for i in range(m):
    item = sys.stdin.readline().strip()
    if item.isdigit() == True:
        print(pint[int(item)-1])
    else:
        print(pname[item]+1)