def solution(lottos, win_nums):
    ans = []
    cnt = 7
    
    for i in lottos:
        if i == 0: 
            cnt -= 1
        elif i in win_nums: 
            cnt -= 1
    if cnt > 6: 
        ans.append(6)
    else:
        ans.append(cnt)
    cnt = 7
    
    for i in lottos:
        if i in win_nums: 
            cnt -= 1
    if cnt > 6: 
        ans.append(6)
    else:
        ans.append(cnt)
    
    return ans