n = int(input())
def solv():
    global n,a
    a = []
    n = int(input())
    so(2,'1')
    print()
def so(now,ans):
    global a
    if now == n+1:
        cal(ans)
        return
    so(now + 1, ans + ' ' + str(now))
    so(now + 1, ans + '+' + str(now))
    so(now + 1, ans + '-' + str(now))
def cal(ans):
    tmp = ans.replace(' ','')
    if eval(tmp) == 0:
        print(ans)
for i in range(n):
    solv()