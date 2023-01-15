def solution(s):
    ans = 0
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if cnt1 == cnt2:
            ans += 1
            k = i
        if k == i:
            cnt1 += 1
        else:
            cnt2 += 1 
    return ans