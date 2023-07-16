from itertools import combinations
n = [int(input()) for i in range(9)]
johap = list(combinations(n, 7))
for i in johap:
    if sum(i) == 100:
        for j in i:
            print(j)