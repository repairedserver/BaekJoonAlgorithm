n = int(input())
people = {}
for i in range(n):
    a, b = input().split()
    if b == 'enter':
        people[a] = 'enter'
    else:
        if people[a]:
            del people[a]
for i in sorted(people, reverse=True):
    print(i)