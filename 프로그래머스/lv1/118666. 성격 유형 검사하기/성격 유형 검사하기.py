def solution(sur, choices):
    ans = ''
    mbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 
             'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(choices)):
        if choices[i] < 4:
            mbti[sur[i][0]] += (choices[i] * 3) % 4
            
        elif choices[i] > 4:
            mbti[sur[i][1]] += choices[i] % 4
            
    mbti_list = list(mbti.keys())
    
    for i in range(0, len(mbti_list), 2):
        if mbti[mbti_list[i]] > mbti[mbti_list[i+1]]:
            ans += mbti_list[i]
            
        elif mbti[mbti_list[i]] < mbti[mbti_list[i+1]]:
            ans += mbti_list[i+1]
            
        else:
            ans += min(mbti_list[i], mbti_list[i+1])
            
    return ans