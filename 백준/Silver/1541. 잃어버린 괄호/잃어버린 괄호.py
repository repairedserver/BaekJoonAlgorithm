arr = input().split('-')
a = 0
for i in arr[0].split('+'):
    a += int(i)
for j in arr[1:]:
    for k in j.split('+'):
        a -= int(k)
print(a)