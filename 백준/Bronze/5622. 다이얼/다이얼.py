a = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
b = input()

time = 0
for unit in a:  
    for i in unit:
        for x in b:
            if i == x:
                time += a.index(unit)+3
print(time)