p, k = map(int, input().split())
bad = k
for i in range(2, k):
    if p % i == 0:
        if bad > i:
            bad = i
if bad != k:
    print('BAD', bad)
else:
    print('GOOD')