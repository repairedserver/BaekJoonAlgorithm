import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nt = dict()
for i in range(n):
    a = input().strip()
    if len(a) >= m:
        if a in nt:
            nt[a] += 1
        else:
            nt[a] = 1
            
nt = sorted(nt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in nt:
    print(i[0])