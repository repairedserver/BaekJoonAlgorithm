s = list(input())
t = list(input())
a = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        a = True
        break
if a:
    print(1)
else:
    print(0)