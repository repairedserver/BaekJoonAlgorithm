def solution(n):
    ans = []
    res = [[0]*n for i in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1          
            elif i % 3 == 1:
                y += 1            
            elif i % 3 == 2:
                x -= 1
                y -= 1      
            res[x][y] = num
            num += 1
            
    for i in res:
        for j in i:
            if j:
                ans.append(j)
    return ans
