def solution(n):
    nl = list(str(n))
    nl.sort(reverse=True)
    return int(''.join(nl))