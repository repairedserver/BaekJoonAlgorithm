def solution(phone_number):
    num = len(phone_number)
    return '*'*(num-4) + phone_number[-4:]