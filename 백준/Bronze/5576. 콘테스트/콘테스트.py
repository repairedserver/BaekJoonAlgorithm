w = []
k = []
for i in range(10):
    w.append(int(input()))
w.sort(reverse=True)
for i in range(10):
    k.append(int(input()))
k.sort(reverse=True)
print(sum(w[:3]), sum(k[:3]))