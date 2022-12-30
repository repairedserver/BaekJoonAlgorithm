def solution(a, b):
    c = 0
    if a < b:
        for i in range(a, b+1):
            c += i
        return c
    else:
        for i in range(b, a+1):
            c += i
        return c