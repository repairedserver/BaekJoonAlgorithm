def solution(a, b, n):
    ans = 0
    while True:
        if n < a:
            break
        s = n // a * a
        r = n // a * b
        e = n - s
        n = e + r
        ans += r
    return ans