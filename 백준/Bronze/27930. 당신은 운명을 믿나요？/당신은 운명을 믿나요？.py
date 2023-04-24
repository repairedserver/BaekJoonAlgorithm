k = ['K', 'O', "R", 'E', 'A']
y = ['Y', 'O', 'N', 'S', 'E', 'I']
n = list(input())
for i in n:
    if i == k[0]:
        k.remove(i)
        if len(k) == 0:
            print('KOREA')
            break
    if i == y[0]:
        y.remove(i)
        if len(y) == 0:
            print('YONSEI')
            break