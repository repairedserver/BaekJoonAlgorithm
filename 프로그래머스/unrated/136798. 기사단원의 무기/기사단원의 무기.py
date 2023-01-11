def solution(number, limit, power):
    iron = 0
    for i in range(1, number + 1):
        w = 0
        for num in range(1, int(i ** 0.5) + 1):
            if i % num == 0:
                w += 1
                if num ** 2 != i:
                    w += 1
            if w > limit:
                w = power
                break
        iron += w
    return iron