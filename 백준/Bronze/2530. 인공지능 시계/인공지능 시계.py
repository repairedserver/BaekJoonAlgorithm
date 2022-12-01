h,m,s = map(int,input().split())
sec = int(input())
m1 = (s+sec)//60
h1 = (m+m1)//60
print((h+h1)%24,(m+m1)%60,(s+sec)%60)