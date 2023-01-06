def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        ans.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
        ans[i] = ans[i].replace('0', ' ')
        ans[i] = ans[i].replace('1', '#')
    return ans