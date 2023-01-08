import itertools
def pnum(n):
    if n == 0 or n == 1:
        return False
    else:
        for num in range(2, (n // 2) + 1): 
            if n % num == 0:
                return False
        return True
def solution(nums):
    ans = 0
    for i in itertools.combinations(nums, 3):
            if pnum(sum(i)):
                ans += 1
    return ans