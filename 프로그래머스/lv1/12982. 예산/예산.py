def solution(d, budget):
    ans = 0
    d = sorted(d)
    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            ans += 1
    return ans