from collections import deque

def solution(scoville, K):
    ans = 0 
    d = deque()
    scoville.sort()
    s = deque(i for i in scoville)
    
    while (s and s[0] < K) or (d and d[0] < K):
        ans += 1
        
        if len(s) + len(d) <= 1:
            return -1
        
        a = [0] * 2
        for i in range(2):
            if s and d:
                if s[0] < d[0]:
                    a[i] = s.popleft()
                else:
                    a[i] = d.popleft()
            elif s:
                a[i] = s.popleft()
            else:
                a[i] = d.popleft()
            
        d.append(a[0] + a[1]*2)
        
    return ans