n, m = map(int, input().split())
l = []
def yee(cnt):
    if cnt - 1 == m:
        print(' '.join(map(str, l)))
        return
    for i in range(1, n+1):
        l.append(i)
        yee(cnt+1)
        l.pop()
yee(1)