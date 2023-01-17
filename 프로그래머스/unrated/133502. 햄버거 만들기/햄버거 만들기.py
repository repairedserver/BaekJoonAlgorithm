def solution(ingredient):
    a = []
    ans = 0
    for i in ingredient:
        a.append(i)
        if a[-4:] == [1, 2, 3, 1]:
            ans += 1
            for j in range(4):
                a.pop()
    return ans