def solution(arr, n):
    arr.sort(key=lambda i: (abs(i-n), i-n))
    return arr[0]