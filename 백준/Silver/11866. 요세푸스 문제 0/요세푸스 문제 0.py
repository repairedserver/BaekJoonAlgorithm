import sys

input = sys.stdin.readline
n, k = map(int,input().split())
cir = [x for x in range(1,n+1)]
removed = []
now = k-1
while cir:
    removed.append(cir.pop(now))
    if cir:
        now = ((now-1) + k) % len(cir)
print(f'<{", ".join(map(str,removed))}>')