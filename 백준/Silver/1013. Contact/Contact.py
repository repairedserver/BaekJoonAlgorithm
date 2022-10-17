import re
n = int(input())
for i in range(n):
    n1 = input()
    n2 = re.compile('(100+1+|01)+')
    if n2.fullmatch(n1):
        print("YES")
    else:
        print("NO")