def solution(arr):
    ans = []
    ans.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            ans.append(arr[i])
    return ans