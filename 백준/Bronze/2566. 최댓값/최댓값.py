num = 0
row = 0
col = 0
t = [list(map(int, input().split())) for _ in range(9)]
for r in range(9):
    for c in range(9):
        if num <= t[r][c]:
            row = r + 1
            col = c + 1
            num = t[r][c]
print(num)
print(row, col)