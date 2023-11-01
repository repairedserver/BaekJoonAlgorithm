def solution(genres, plays):
    ans = []
    playD = {}
    dic = {}
    for i in range(len(genres)):
        playD[genres[i]] = playD.get(genres[i], 0) + plays[i]
        dic[genres[i]] = dic.get(genres[i], [])+[(plays[i], i)]
        
    s = sorted(playD.items(), key=lambda x: x[1], reverse=True)
    
    for (i, j) in s:
        dic[i] = sorted(dic[i], key=lambda x: (-x[0], x[1]))
        ans += [b for (a, b) in dic[i][:2]]
    
    return ans