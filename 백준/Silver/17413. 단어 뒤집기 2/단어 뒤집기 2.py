w = list(input().rstrip())
i = 0
st = 0
while i < len(w):
    if w[i] == "<":
        i += 1 
        while w[i] != ">":
            i += 1 
        i += 1
    elif w[i].isalnum():
        st = i
        while i < len(w) and w[i].isalnum():
            i += 1
        tmp = w[st:i]
        tmp.reverse()
        w[st:i] = tmp
    else:
        i += 1
print("".join(w))