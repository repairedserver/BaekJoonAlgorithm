n = int(input())
m = input()
cnt = m.count('LL')

if cnt <= 1:
    print(len(m))
else:
    print(len(m)-cnt+1)