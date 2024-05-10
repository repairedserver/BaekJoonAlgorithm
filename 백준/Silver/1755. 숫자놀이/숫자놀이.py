n, m = map(int, input().split())
d = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
     '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
l = []
for i in range(n, m+1):
    a = ''.join([d[j] for j in str(i)])
    l.append([i, a])

l.sort(key=lambda x: x[1])
for i in range(len(l)):
    if i%10 == 0 and i!= 0:
        print()
    print(l[i][0], end=' ')