def solution(numbers):
    n = [str(i) for i in numbers]
    n.sort(key=lambda num: num*3, reverse=True)
    return str(int(''.join(n)))