n = input()
r = ''
for i in range(len(n)):
    if n[i] == ' ' or ord(n[i]) < ord('A'):
        r += n[i]
    else:
        if ord(n[i])+13 > 122:
            r += chr(96+(ord(n[i])+13)-122)
        elif ord(n[i])+13 > 90 and ord(n[i]) < 91:
            r += chr(64+(ord(n[i])+13)-90)
        else:
            r += chr(ord(n[i])+13)
print(r)