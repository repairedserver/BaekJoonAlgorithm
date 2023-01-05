def solution(strings, n):
    ans1 = []
    ans2 = []
    for i in strings:
        ans1.append(i[n]+i)
    ans1.sort()
    for i in ans1:
        ans2.append(i[1:])
    return ans2