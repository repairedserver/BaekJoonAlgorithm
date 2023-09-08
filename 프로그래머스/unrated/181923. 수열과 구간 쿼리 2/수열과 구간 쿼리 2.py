def solution(arr, queries):
    ans = []
    for q in queries:
        temp = []
        for i in range(q[0], q[1]+1):
            if arr[i] > q[2]:
                temp.append(arr[i])
        try:
            ans.append(min(temp))
        except:
            ans.append(-1)
    return ans