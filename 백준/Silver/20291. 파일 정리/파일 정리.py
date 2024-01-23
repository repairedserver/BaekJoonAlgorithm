dic = dict()
for i in range(int(input())):
    n = (input().split('.'))[1]
    if not n in dic:
        dic[n] = 1
    else:
        dic[n] += 1

srt = sorted(dic.items())
for i, j in srt:
    print(i, j)