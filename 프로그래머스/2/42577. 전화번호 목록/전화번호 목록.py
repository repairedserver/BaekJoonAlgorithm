def solution(phone_book):
    h = {}
    for i in phone_book:
        h[i] = 1
    for i in phone_book:
        a = ""
        for num in i:
            a += num
            if a in h and a != i:
                return False
    return True