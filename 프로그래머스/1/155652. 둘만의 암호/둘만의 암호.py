def solution(s, skip, index):
    ans = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alpha = alpha.replace(i, '')
    for i in s:
        ans += alpha[(alpha.index(i)+index) % len(alpha)]
    return ans