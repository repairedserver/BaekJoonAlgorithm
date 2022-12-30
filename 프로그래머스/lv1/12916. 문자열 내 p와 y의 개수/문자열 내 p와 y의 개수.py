def solution(s):
    a = 0
    b = 0
    s = list(s)
    for i in s:
        if i == 'p' or i == 'P':
            a += 1
        elif i == 'y' or i == 'Y':
            b += 1
    
    if a == b:
        return True
    elif a == 0 and b == 0:
        return True
    else:
        return False

    return True