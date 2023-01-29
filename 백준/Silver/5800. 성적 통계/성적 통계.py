n = int(input())
num = 1
for i in range(n):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    score = sorted(arr[1::], reverse=True)
    max_ = max(score)
    min_ = min(score)
    gap = score[0] - score[1]
    for i in range(2, len(score)):
        gap = max(gap, score[i - 1] - score[i])
    print('Class', num)
    print('Max', max_, end=", ")
    print('Min', min_, end=", ")
    print('Largest gap', gap)
    num += 1