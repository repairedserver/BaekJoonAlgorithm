n = int(input())
score = []
cnt = 0
for i in range(n):
    score.append(int(input()))
for i in range(n - 2, -1, -1):
    if score[i] >= score[i + 1]:
        cnt += score[i] - score[i + 1] + 1
        score[i] = score[i + 1] - 1
print(cnt)