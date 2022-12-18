import sys
input = sys.stdin.readline
n = int(input())
num = []
for i in range(0, n):
    num.append(int(input()))
num.sort()
num.reverse()
for i in range(0, n):
    print(num[i])