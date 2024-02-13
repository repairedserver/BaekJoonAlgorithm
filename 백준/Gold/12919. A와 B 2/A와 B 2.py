def dfs(s,t):
    ans = 0
    if s == t:
        return 1
    if len(t) <= len(s):
        return 0
    if t[-1] == 'A':
        ans = dfs(s, t[:-1])
    if ans == 1:
        return 1

    if t[0]=='B':
        ans = dfs(s,t[::-1][:-1])
        
    return ans

s = list(input())
t = list(input())
print(dfs(s, t))