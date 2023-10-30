def solution(clothes):
    ans = 1
    h = {}
    for a, b in clothes:
        h[b] = h.get(b, 0)+1    
    for i in h:
        ans *= (h[i]+1)
    return ans-1