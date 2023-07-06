import sys
input = sys.stdin.readline
num = [True for i in range(246913)]
for i in range(2, int(246912**0.5)+1):
            for j in range(i*2, 246913, i):
                num[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        cnt = 0
        for i in range(n+1, (2*n)+1, 1):
            if num[i] == True:
                cnt += 1
        print(cnt)