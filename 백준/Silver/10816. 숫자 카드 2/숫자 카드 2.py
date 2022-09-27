from sys import stdin

n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
t = list(map(int,stdin.readline().split()))

ha = {}

for i in card:
    if i in ha:
        ha[i] += 1
    else:
        ha[i] = 1

for i in t:
    if i in ha:
        print(ha[i], end=' ')
    else:
        print(0, end=' ')