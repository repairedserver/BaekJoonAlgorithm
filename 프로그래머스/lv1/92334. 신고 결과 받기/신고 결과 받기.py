def solution(id_list, report, k):
    cnt = {i: 0 for i in id_list}
    ans = [0 for i in range(len(id_list))]
    
    for i in set(report):
        cnt[i.split()[1]] += 1
            
    for i in set(report):
        if cnt[i.split()[1]] >= k:
            ans[id_list.index(i.split()[0])] += 1
    
    return ans