def solution(array, cmd):
    ans = []
    for i in range(len(cmd)):
        arr = array[cmd[i][0]-1:cmd[i][1]]
        arr.sort()
        ans.append(arr[cmd[i][2]-1])
    return ans