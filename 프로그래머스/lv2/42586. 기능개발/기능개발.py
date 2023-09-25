def solution(progresses, speeds):
    day = 0
    cnt = 0
    ans = []
    while 0 < len(progresses):
        if 100 <= progresses[0] + speeds[0] * day:
            speeds.pop(0)
            progresses.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                ans.append(cnt)
                cnt = 0
            else:
                day += 1
    ans.append(cnt)
    return ans