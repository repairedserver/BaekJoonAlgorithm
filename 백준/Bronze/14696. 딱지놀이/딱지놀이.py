n = int(input())
for i in range(n):
    la = list(map(int, input().split()))[1:]
    lb = list(map(int, input().split()))[1:]
    for j in range(4,0,-1):
        if la.count(j) > lb.count(j):
            print("A")
            break
        elif la.count(j) < lb.count(j):
            print("B")
            break
        if j == 1:
            print("D")