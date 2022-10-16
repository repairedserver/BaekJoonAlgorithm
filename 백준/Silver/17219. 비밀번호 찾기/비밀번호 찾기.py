n, m = map(int, input().split())
me = {}

for i in range(n):
    key, val = input().split()
    me[key] = val

for j in range(m):
    key = input().strip()
    print(me[key])