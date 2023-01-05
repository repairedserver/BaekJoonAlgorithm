import itertools
def solution(num):
    ans = []
    ans1 = []
    num = list(itertools.permutations(num, 2))
    for i in range(len(num)):
        ans.append(sum(num[i]))
    ans.sort()
    for i in ans:
        if i not in ans1:
            ans1.append(i)
    return ans1