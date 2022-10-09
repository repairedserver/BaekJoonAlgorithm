t = int(input())
 
for i in range(t):
    cnt1 = [1,0]
    cnt2 = [0,1]
    n = int(input())
    if n > 1:
        for j in range(n-1):
            cnt1.append(cnt2[-1])
            cnt2.append(cnt1[-2]+cnt2[-1])
    print(cnt1[n], cnt2[n])