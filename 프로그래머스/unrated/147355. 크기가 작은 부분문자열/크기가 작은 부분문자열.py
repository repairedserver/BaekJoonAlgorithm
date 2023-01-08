def solution(t, p):
    cnt = 0
    for i in range(0, len(t) + 1 - len(p)):
        if int(t[i:i+len(p)]) <= int(p):
            cnt += 1
    return cnt