import sys
input = sys.stdin.readline

n_k, n_p = map(int, input().split(' '))
cnt = 0
m = {}

for i in range(n_k):
    m[input().rstrip()] = 1
    cnt += 1

for i in range(n_p):
    post = list(input().rstrip().split(','))
    for j in post:
        if j in m.keys():
            if m[j] == 1:
                m[j] = 0
                cnt -= 1
    print(cnt)