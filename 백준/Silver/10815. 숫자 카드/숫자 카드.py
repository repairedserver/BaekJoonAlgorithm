n = map(int, input())
my = sorted(map(int, input().split()))
m = map(int, input())
num = list(map(int, input().split()))
ans = []

def bi(k, my, st, end):
    mid = (st+end) // 2
    if st > end:
        ans.append(str(0))
    elif k == my[mid]:
        ans.append(str(1))
    elif k > my[mid]:
        bi(k, my, mid+1, end)
    else:
        bi(k, my, st, mid-1)

for k in num:
    st = 0
    end = len(my)-1
    bi(k, my, st, end)

print(' '.join(ans))