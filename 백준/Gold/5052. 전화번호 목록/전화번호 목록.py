import sys
input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    c = [str(input().strip()) for j in range(n)]
    c.sort()
    chek = "y"
    for j in range(len(c) - 1):
        if c[j] == c[j + 1][0:len(c[j])]:
            chek = "n"
    print('NO') if chek == "n" else print('YES')