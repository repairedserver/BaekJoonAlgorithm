def solution(num_list, n):
    ans = []
    for i in range(len(num_list)//n):
        ans.append(num_list[i*n:(i+1)*n])
    return ans