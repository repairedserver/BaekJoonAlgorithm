def solution(n, m):
    ans = []
    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            ans.append(i)
            break
    return ans + [n * m // ans[0]]