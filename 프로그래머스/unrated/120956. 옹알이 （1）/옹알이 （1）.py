def solution(babbling):
    res = 0
    for i in babbling:
        cnt = 0
        w = ''
        for j in i:
            w += j
            if w in ['aya', 'ye', 'woo', 'ma']:
                w = ''
                cnt += 1
        if len(w) == 0 and cnt > 0:
                res += 1  
    return res