def solution(s):
    s = s.split(' ')
    ans = []
    
    for i in range(len(s)):
        res = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                res += s[i][j].upper()
            else:
                res += s[i][j].lower()

        ans.append(res)

    return ' '.join(ans)