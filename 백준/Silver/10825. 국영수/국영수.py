import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a,b,c,d = list(map(str, input().split()))
    arr.append([a,int(b),int(c),int(d)])
    
arr.sort(key = lambda i : (-i[1] , i[2],-i[3],i[0]))
for i in arr:
    print(i[0])