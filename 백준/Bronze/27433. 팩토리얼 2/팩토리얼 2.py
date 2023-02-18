a = int(input()) 
if a == 0:
    print(1)
else:
    b = 1
    for i in range(2, a+1):
        b *= i
    print(b)