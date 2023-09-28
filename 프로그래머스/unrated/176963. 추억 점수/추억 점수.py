def solution(name, yearning, photo):
    ans = []
    for i in photo:
        a = 0
        for n in i:
            if n in name:
                a += yearning[name.index(n)]
        ans.append(a)
    return ans