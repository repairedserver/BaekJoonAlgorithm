n, m = list(map(int,input().split()))
s = []
def yee(st):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(st,n+1):
        if i not in s:
            s.append(i)
            yee(i+1)
            s.pop()
yee(1)