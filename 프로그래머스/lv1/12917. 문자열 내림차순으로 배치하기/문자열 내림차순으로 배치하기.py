def solution(s):
    a = ''
    b = sorted(s, reverse=True) 
    for i in b:
        a += i
    return a