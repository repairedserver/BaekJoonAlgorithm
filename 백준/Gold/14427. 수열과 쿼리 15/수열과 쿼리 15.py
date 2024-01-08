import sys
input = sys.stdin.readline

def init(st, end, idx):
    if st == end:
        t[idx] = arr[st]
    else:
        mid = (st+end) // 2
        t[idx] = min(init(st, mid, idx*2), init(mid+1, end, idx*2+1))
    return t[idx]

def ud(st, end, idx, w, v):
    if w < st or end < w:
        return 
    if st == end:
        t[idx] = v
        return t[idx]
    mid = (st+end) // 2
    ud(st, mid, idx*2, w, v)
    ud(mid+1, end, idx*2+1, w, v)
    t[idx] = min(t[idx*2], t[idx*2+1])
    
def fm(st, end, idx, left, right):
    if right < st or end < left:
        return [float('inf'), float('inf')]
    if left <= st and end <= right:
        return t[idx]
    mid = (st+end) // 2
    return min(fm(st, mid, idx*2+1, left, right), fm(mid+1, end, idx*2, left, right))

n = int(input())
l = list(map(int,input().split()))
t = [0]*(n*4)
arr = []

for i in range(n):
    arr.append([l[i],i+1])

init(0, n-1, 1)

for i in range(int(input())):
    l = list(map(int,input().split()))
    if l[0] == 2:
        print(fm(0, n-1, 1, 0, n-1)[1])
    elif l[0] == 1:
        arr[l[1]-1][0]=l[2]
        ud(0, n-1, 1, l[1]-1, arr[l[1]-1])