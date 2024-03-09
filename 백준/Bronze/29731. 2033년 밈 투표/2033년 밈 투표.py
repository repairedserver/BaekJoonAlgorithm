gongyak = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']
a = []
for i in range(int(input())):
    a.append(input())
for i in a:
    if i in gongyak:
        continue
    else:
        print('Yes')
        exit()
print('No')