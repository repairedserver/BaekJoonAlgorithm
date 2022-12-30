def solution(n):
    answer = []
    n = reversed(str(n))
    for i in n:
        answer.append(i)
    return list(map(int, answer))