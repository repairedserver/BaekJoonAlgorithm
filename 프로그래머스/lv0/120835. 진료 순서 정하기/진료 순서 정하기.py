def solution(emergency):
    ans = []
    s = sorted(emergency, reverse=True)
    for e in emergency:
        i = s.index(e)+1
        ans.append(i)
    return ans