def solution(arr):
    stk = []
    i = 0
    while len(arr) > i:
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and arr[i] > stk[-1]:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0 and arr[i] <= stk[-1]:
            stk.pop()
    return stk
