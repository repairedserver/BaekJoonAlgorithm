n = input().replace(' ','')
ans = 'UCPC'
cnt = 0
for i in n:
    if i == ans[cnt]:
        cnt += 1
    if cnt == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')