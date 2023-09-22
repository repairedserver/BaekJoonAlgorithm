def solution(quiz):
    ans = []
    for q in quiz:
        l, r = q.split('=')
        l = l.split()
        if l[1] == '+':
            if int(l[0])+int(l[2]) == int(r):
                ans.append('O')
            else:
                ans.append('X')
        elif l[1] == '-':
            if int(l[0])-int(l[2]) == int(r):
                ans.append('O')
            else:
                ans.append('X')
    return ans