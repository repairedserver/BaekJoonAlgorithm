def solution(k, m, score):
    score.sort()
    ans = 0
    for i in range(len(score), m-1, -m):
        ans += score[i - m] * m
    return ans