import sys
input = sys.stdin.readline
n = int(input())
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
res = []
for i in range(n):
    cnt = ""
    m = list(map(str, input().strip("\n")))
    t = []
    for j in m:
        if j in nums:
            cnt += j
        else:
            if cnt:
                t.append(int(cnt))
                cnt = ""
    if cnt:
        t.append(int(cnt))
    res += t
res.sort()
for i in res:
    print(i)