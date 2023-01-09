def solution(N, stages):
    ans = []
    length = len(stages)
    for i in range(1, N+1):
        cnt = stages.count(i)
        if length == 0:
            f = 0
        else:
            f = cnt / length
        length -= cnt
        ans.append((i, f))
    ans = sorted(ans, key=lambda x: x[1], reverse=True)
    ans = [i[0] for i in ans]
    return ans
            
    return ans