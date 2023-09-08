def solution(numbers):
    cnt = 0
    for i in range(9):
        if not i+1 in numbers:
            cnt += (i + 1)
    return cnt