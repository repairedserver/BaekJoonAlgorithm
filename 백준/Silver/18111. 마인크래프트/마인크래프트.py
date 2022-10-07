import sys
input = sys.stdin.readline
max_height = 256
min_height = 0
n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
h_cnt = [0 for _ in range(max_height + 1)]
ans_cost = 100000001
ans_height = 0
sum_height = b

for row in board:
    for val in row:
        h_cnt[val] += 1
        sum_height += val
        
min_h = min([min(row) for row in board])
max_h = sum_height // (n * m)

for h in range(min_h, max_h+1):
    cost = 0
    usable_blocks = b
    for i in range(min_height, max_height+1 ):
        if h < i:
            cost += h_cnt[i] * abs(h - i) * 2
            usable_blocks += h_cnt[i] * abs(h - i)
        else:
            cost += h_cnt[i] * abs(h - i)
            usable_blocks -= h_cnt[i] * abs(h - i)
            
    if cost <= ans_cost and usable_blocks >= 0:
        ans_cost = cost
        ans_height = h

print(ans_cost, ans_height)