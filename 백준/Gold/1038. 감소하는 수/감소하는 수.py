def add(d, n):
    if d == 1:
        decre.append(n)
    else:
        for i in range(n%10):
            add(d-1, n*10+i)

def back(d):
    for i in range(d-1, 10):
        add(d, i)
        
decre = []

for i in range(11):
    back(i)
    
n = int(input())
if n >= len(decre):
    print(-1)
else:
    print(decre[n])