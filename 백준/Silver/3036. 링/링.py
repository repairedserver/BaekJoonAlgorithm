n = int(input())
r = list(map(int, input().split()))
d = r[0]

def findGCD(a, b):
    num = b
    d = a
    rest = b % a
    while rest != 0:
        num = d
        d = rest
        rest = num % d
    return d

for i in range(1, n):
    d_i = r[i]
    GCD = findGCD(d, d_i)
    print(f'{d//GCD}/{d_i//GCD}')