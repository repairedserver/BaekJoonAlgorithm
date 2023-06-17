a = [] 
for i in range(6):  
    a.append(int(input())) 
b = sorted(a[:4])
print(sum(b[1:]) + max(a[4:]))