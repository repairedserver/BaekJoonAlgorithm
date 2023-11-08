def solution(N, number):
    dp = [set() for i in range(9)]
    N = str(N)
    for i in range(1, 9):
        dp[i].add(int(N*i))
        
        for j in range(i//2 + 1):
            for f in dp[j]:
                for s in dp[i-j]:
                    dp[i].add(f+s)
                    dp[i].add(f-s)
                    dp[i].add(s-f)
                    dp[i].add(f*s)
                    
                    if f != 0:
                        dp[i].add(s//f)
                    if s != 0:
                        dp[i].add(f//s)
                        
        if number in dp[i]:
            return i
    return -1