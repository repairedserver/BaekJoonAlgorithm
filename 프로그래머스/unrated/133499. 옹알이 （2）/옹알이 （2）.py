def solution(babbling):
    cnt = 0
    s = ["aya", "ye", "woo", "ma"]     
    for i in babbling:                
        for j in s:               
            if j * 2 not in i:           
                i = i.replace(j, ' ')     
        if i.strip() == '':   
            cnt += 1                  
    return cnt