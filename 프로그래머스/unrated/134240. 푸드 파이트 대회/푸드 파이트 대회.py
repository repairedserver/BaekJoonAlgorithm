def solution(f):
    ans = '0'
    for i in range(len(f) - 1, 0, -1):
        ans = str(i) * (f[i] // 2) + ans
        ans = ans + str(i) * (f[i] // 2)
    return ans