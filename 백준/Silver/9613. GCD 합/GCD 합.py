import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

for i in range(int(input())):
    r = list(map(int, input().split()))
    s = len(r)
    t = 0
    for j in range(1, s):
        for k in range(j+1, s):
            t += gcd(r[j], r[k])
    print(t)