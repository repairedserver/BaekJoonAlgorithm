import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, input().split()))

st, e = 0, max(trees)

while st <= e:
    mid = (st+e)//2
    tree = 0
    for i in trees:
        if i > mid:
            tree += i - mid

    if tree >= m: 
        st = mid + 1
    else:
        e = mid - 1
print(e)