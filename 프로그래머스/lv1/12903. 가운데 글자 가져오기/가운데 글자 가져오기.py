def solution(s):
    n = len(s)
    if n % 2 == 0:
        return s[n - (n // 2) - 1 : n - (n // 2) + 1]
    else:
        return s[n // 2]