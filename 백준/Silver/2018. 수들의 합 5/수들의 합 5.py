n = int(input())
st, en = 1, 1
cnt, t = 0, 1

while en != n:
    if t < n:
        en += 1
        t += en
    elif t > n:
        t -= st
        st += 1
    else:
        cnt += 1
        en += 1
        t += en
print(cnt + 1)