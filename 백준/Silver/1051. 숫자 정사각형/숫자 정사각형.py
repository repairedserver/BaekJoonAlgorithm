import sys
input = sys.stdin.readline
def square(s):
    for i in range(n-s+1):
        for j in range(m-s+1):
            if num[i][j] == num[i][j+s-1] == num[i+s-1][j] == num[i+s-1][j+s-1]:
                return True
    return False
n, m = map(int, input().split())
num = []
for i in range(n):
    num.append(list(input()))
for i in range(min(n, m), 0, -1):
    if square(i) == True:
        print(i**2)
        break