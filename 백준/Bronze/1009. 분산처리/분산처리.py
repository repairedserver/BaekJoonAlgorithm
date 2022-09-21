n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    a %= 10
    
    if a == 0:
        print(10)
    elif a == 1 | a == 5 | a == 6:
        print(a)
    elif a == 4 | a == 2:
        b %= 2
        if b == 1:
            print(a)
        else:
            print((a*a)%10)
            
    else:
        b = b % 4
        if b == 0:
            print((a**4) % 10 % 10 % 10)
        else:
            print((a**b) % 10 % 10 % 10)
