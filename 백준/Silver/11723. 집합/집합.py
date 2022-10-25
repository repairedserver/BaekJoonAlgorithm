import sys
input = sys.stdin.readline
n = int(input())
s = set()
for a in range(n):
    c = input().split()
    if c[0] == "all":
        s = set([i for i in range(1, 21)])
    elif c[0] == "empty":
        s = set()
    elif c[0] == "add":
        s.add(int(c[1]))
    elif c[0] == "check":
        print (1 if int(c[1]) in s else 0)
    elif c[0] == "remove":
        s.discard(int(c[1]))
    elif c[0] == "toggle":
        if int(c[1]) in s:
            s.discard(int(c[1]))
        else:
            s.add(int(c[1]))