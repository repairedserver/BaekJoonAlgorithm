n = int(input())
n_ = []
for i in range(n):
    n_.append(int(input()))
c = n_[1:len(n_)]
d = n_[0]  
if(n == 1):
    print(0)
else:
    num = 0
    c = sorted(c, reverse = True)
    while(c[0] >= d):
        d += 1
        c[0] -= 1
        num += 1
        c = sorted(c, reverse = True)
    print(num)