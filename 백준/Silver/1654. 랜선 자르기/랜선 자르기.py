import sys
input = sys.stdin.readline

def binary_search(low, high):
    global n
    global ans
    if high < low:
        return
    mid = (low+high) // 2
    t = 0
    for i in l:
        t += i//mid
    if t >= n:
        ans = mid   
        binary_search(mid+1, high)
    else:
        binary_search(low, mid-1)
        
k, n = map(int, input().split())
l = []
for i in range(k):
    l.append(int(input()))
l_max = max(l)
ans = 0
binary_search(0, l_max*2)
print(ans)