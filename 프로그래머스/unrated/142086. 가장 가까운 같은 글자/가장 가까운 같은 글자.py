def solution(s):
    ans = []
    word = {}
    for i, j in enumerate(list(s)):
        if j not in word:
            ans.append(-1)
            word[j] = i
        else:
            ans.append(i - word[j])
            word[j] = i
    return ans