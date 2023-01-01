def solution(arr):
    arr.pop(arr.index(min(arr)))
    if len(arr) == 0:
        arr.append(-1)
    return arr