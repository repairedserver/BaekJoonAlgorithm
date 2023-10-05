def dfs(num, target, d):
    ans = 0
    if d == len(num):
        if sum(num) == target:
            return 1
        else: 
            return 0
    else:
        ans += dfs(num, target, d+1)
        num[d] *= -1
        ans += dfs(num, target, d+1)
        return ans
    
def solution(num, target):
    ans = dfs(num, target, 0)
    return ans