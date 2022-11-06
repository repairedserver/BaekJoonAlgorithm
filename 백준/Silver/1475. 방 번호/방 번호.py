n = input()
ans = [0] * 10
for i in range(len(n)):
    n1 = int(n[i])
    if n1 == 6 or n1 == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[n1] += 1
print(max(ans))