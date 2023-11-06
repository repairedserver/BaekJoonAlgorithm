def solution(cap, n, deliveries, pickups):
    ans = 0
    d = deliveries[::-1]
    p = pickups[::-1]
    deli = 0
    pick = 0

    for i in range(n):
        deli += d[i]
        pick += p[i]
        
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            ans += (n-i)*2

    return ans