def solution(price, money, count):
    n = 0
    for i in range(1, count+1):
        n += i * price
    if n >= money:
        return n - money
    else:
        return 0