n = input()
l = [0] * 26
for i in n:
    l[ord(i)-97] += 1
    
for i in l:
    print(i)