n = input()
real = ''
for i in n:
    if 68 <= ord(i) <= 91:
        real += chr(ord(i) - 3)
    else:
        real += chr(ord(i) + 23)
print(real)