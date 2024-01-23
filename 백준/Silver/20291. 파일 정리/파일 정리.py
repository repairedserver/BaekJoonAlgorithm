import sys
input = sys.stdin.readline
dic = {}

for i in range(int(input())):
    n = (input().rstrip().split("."))[1]
    dic[n] = dic.get(n, 0) + 1

srt = sorted(dic)
  
for i in range(len(srt)):
    e = srt[i]
    print(e, dic[e])